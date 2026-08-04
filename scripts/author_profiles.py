"""Author identity resolution and generated author profile data.

The hand-maintained profile registry lives in ``author_profiles``.  This
module deliberately has no dependency on ``update.py`` so its identity and
aggregation rules can be unit tested without running a website import.
"""

from __future__ import annotations

import copy
import hashlib
import json
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

import yaml


DEFAULT_EXAMPLE_LICENSE = "CC0-1.0"
DEFAULT_EXAMPLE_LICENSE_URL = "https://creativecommons.org/publicdomain/zero/1.0/"
DEFAULT_EXAMPLE_AUTHOR = "Defold Foundation"
DEFAULT_AVATAR = "/images/icons/community-assets-on-dark.svg"
MAX_BIO_LENGTH = 280

ALLOWED_LINK_TYPES = {
    "website",
    "x",
    "bluesky",
    "mastodon",
    "linkedin",
}
SUPPORT_DESTINATIONS = {
    "github_sponsors": ("github.com", "/sponsors/"),
    "ko_fi": ("ko-fi.com", "/"),
    "patreon": ("patreon.com", "/"),
    "buy_me_a_coffee": ("buymeacoffee.com", "/"),
    "paypal": ("paypal.me", "/"),
}
GITHUB_USERNAME_RE = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


class AuthorProfileValidationError(ValueError):
    """Raised when the website-owned profile registry is malformed."""


def canonical_author_id(name: str) -> str:
    """Return the stable author URL id used by the existing website."""

    return hashlib.md5(name.encode("utf-8")).hexdigest()


def _clean_name(value: object, label: str = "author name") -> str:
    if not isinstance(value, str):
        raise AuthorProfileValidationError(f"{label} must be a string")
    value = re.sub(r"\s+", " ", value).strip()
    if not value:
        raise AuthorProfileValidationError(f"{label} must not be empty")
    return value


def _validate_https_url(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AuthorProfileValidationError(f"{label} must be a non-empty string")
    value = value.strip()
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.hostname:
        raise AuthorProfileValidationError(f"{label} must be an absolute https URL")
    if parsed.username or parsed.password:
        raise AuthorProfileValidationError(f"{label} must not contain credentials")
    return value


def _validate_avatar(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AuthorProfileValidationError(f"{label} must be a non-empty string")
    value = value.strip()
    if value.startswith("/") and not value.startswith("//") and ".." not in value.split("/"):
        return value
    return _validate_https_url(value, label)


def _validate_links(value: object, profile_name: str) -> list[dict]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise AuthorProfileValidationError(f"{profile_name}: links must be an array")

    result = []
    for index, item in enumerate(value):
        label = f"{profile_name}: links[{index}]"
        if not isinstance(item, dict):
            raise AuthorProfileValidationError(f"{label} must be an object")
        link_type = item.get("type")
        if link_type not in ALLOWED_LINK_TYPES:
            raise AuthorProfileValidationError(
                f"{label}.type must be one of {', '.join(sorted(ALLOWED_LINK_TYPES))}"
            )
        link = {
            "type": link_type,
            "url": _validate_https_url(item.get("url"), f"{label}.url"),
        }
        if item.get("label") is not None:
            link["label"] = _clean_name(item["label"], f"{label}.label")
        result.append(link)
    return result


def _validate_support(value: object, profile_name: str) -> list[dict]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise AuthorProfileValidationError(f"{profile_name}: support must be an array")
    if len(value) > 3:
        raise AuthorProfileValidationError(f"{profile_name}: support allows at most three actions")

    result = []
    for index, item in enumerate(value):
        label = f"{profile_name}: support[{index}]"
        if not isinstance(item, dict):
            raise AuthorProfileValidationError(f"{label} must be an object")
        support_type = item.get("type")
        if support_type not in SUPPORT_DESTINATIONS:
            raise AuthorProfileValidationError(
                f"{label}.type must be one of {', '.join(sorted(SUPPORT_DESTINATIONS))}"
            )
        url = _validate_https_url(item.get("url"), f"{label}.url")
        parsed = urlparse(url)
        expected_host, required_path = SUPPORT_DESTINATIONS[support_type]
        hostname = (parsed.hostname or "").lower()
        if hostname == f"www.{expected_host}":
            hostname = expected_host
        if hostname != expected_host or not parsed.path.startswith(required_path):
            raise AuthorProfileValidationError(
                f"{label}.url is not an allowed {support_type} destination"
            )
        support = {"type": support_type, "url": url}
        if item.get("label") is not None:
            support["label"] = _clean_name(item["label"], f"{label}.label")
        result.append(support)
    return result


def _normalise_profile(raw: object, source: str) -> dict:
    if not isinstance(raw, dict):
        raise AuthorProfileValidationError(f"{source}: profile must be an object")

    name = _clean_name(raw.get("name"), f"{source}: name")
    allowed_fields = {"name", "github", "aliases", "bio", "avatar", "links", "support"}
    unknown_fields = sorted(set(raw) - allowed_fields)
    if unknown_fields:
        raise AuthorProfileValidationError(
            f"{source}: unknown profile field(s): {', '.join(unknown_fields)}"
        )

    profile = {
        "id": canonical_author_id(name),
        "name": name,
        "aliases": [],
        "links": _validate_links(raw.get("links"), name),
        "support": _validate_support(raw.get("support"), name),
    }

    github = raw.get("github")
    if github is not None:
        github = _clean_name(github, f"{name}: github").lstrip("@")
        if not GITHUB_USERNAME_RE.fullmatch(github):
            raise AuthorProfileValidationError(f"{name}: malformed GitHub username")
        profile["github"] = github

    aliases = raw.get("aliases", [])
    if not isinstance(aliases, list):
        raise AuthorProfileValidationError(f"{name}: aliases must be an array")
    exact_aliases = set()
    for index, alias in enumerate(aliases):
        alias = _clean_name(alias, f"{name}: aliases[{index}]")
        if alias in exact_aliases:
            raise AuthorProfileValidationError(f"{name}: duplicate alias {alias!r}")
        exact_aliases.add(alias)
        if alias != name:
            profile["aliases"].append(alias)

    bio = raw.get("bio")
    if bio is not None:
        bio = _clean_name(bio, f"{name}: bio")
        if len(bio) > MAX_BIO_LENGTH:
            raise AuthorProfileValidationError(
                f"{name}: bio must be at most {MAX_BIO_LENGTH} characters"
            )
        profile["bio"] = bio

    avatar = raw.get("avatar")
    if avatar is not None:
        profile["avatar"] = _validate_avatar(avatar, f"{name}: avatar")

    return profile


def load_profile_records(profile_dir: os.PathLike | str) -> list[dict]:
    """Load and validate every JSON registry file in ``profile_dir``."""

    profile_dir = Path(profile_dir)
    if not profile_dir.is_dir():
        raise AuthorProfileValidationError(f"Author profile directory does not exist: {profile_dir}")

    profiles = []
    for path in sorted(profile_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise AuthorProfileValidationError(f"{path}: invalid JSON: {error}") from error
        records = data if isinstance(data, list) else [data]
        for index, record in enumerate(records):
            profiles.append(_normalise_profile(record, f"{path}[{index}]"))
    if not profiles:
        raise AuthorProfileValidationError(f"No author profiles found in {profile_dir}")
    return profiles


class AuthorRegistry:
    """Case-insensitive canonical, GitHub username, and alias resolver."""

    def __init__(self, profiles: list[dict]):
        self.profiles = [copy.deepcopy(profile) for profile in profiles]
        self._lookup: dict[str, dict] = {}
        self._unknown: dict[str, dict] = {}

        for profile in self.profiles:
            identities = [profile["name"], profile.get("github"), *profile.get("aliases", [])]
            for identity in identities:
                if not identity:
                    continue
                key = identity.casefold()
                existing = self._lookup.get(key)
                if existing and existing["id"] != profile["id"]:
                    raise AuthorProfileValidationError(
                        f"Duplicate author identity {identity!r} belongs to both "
                        f"{existing['name']!r} and {profile['name']!r}"
                    )
                self._lookup[key] = profile

    @classmethod
    def load(cls, profile_dir: os.PathLike | str) -> "AuthorRegistry":
        return cls(load_profile_records(profile_dir))

    def find(self, name: object) -> dict | None:
        if not isinstance(name, str) or not name.strip():
            return None
        cleaned = re.sub(r"\s+", " ", name).strip().lstrip("@")
        profile = self._lookup.get(cleaned.casefold())
        return copy.deepcopy(profile) if profile else None

    def is_registered(self, name: object) -> bool:
        return self.find(name) is not None

    def resolve(self, name: object) -> dict:
        cleaned = _clean_name(name)
        lookup_name = cleaned.lstrip("@")
        profile = self._lookup.get(lookup_name.casefold())
        if profile:
            return copy.deepcopy(profile)

        key = cleaned.casefold()
        if key not in self._unknown:
            self._unknown[key] = {
                "id": canonical_author_id(cleaned),
                "name": cleaned,
                "aliases": [],
                "links": [],
                "support": [],
            }
        return copy.deepcopy(self._unknown[key])


def example_author_names(example: dict, registry: AuthorRegistry | None = None) -> list[str]:
    """Read preferred ``authors`` or legacy ``author`` example metadata."""

    preferred = example.get("authors")
    if isinstance(preferred, list) and preferred:
        names = []
        for item in preferred:
            value = item.get("name") if isinstance(item, dict) else item
            names.append(_clean_name(value, "example author"))
        return names

    legacy = example.get("author")
    if legacy is None or (isinstance(legacy, str) and not legacy.strip()):
        return [DEFAULT_EXAMPLE_AUTHOR]
    if isinstance(legacy, list):
        return [_clean_name(value, "example author") for value in legacy]
    legacy = _clean_name(legacy, "example author")

    # Older examples used comma-separated contributor strings.  Preserve a
    # registered full name containing a comma, otherwise treat it as multiple
    # legacy authors.
    if "," in legacy and not (registry and registry.is_registered(legacy)):
        return [_clean_name(value, "example author") for value in legacy.split(",")]
    return [legacy]


def _public_author_reference(profile: dict) -> dict:
    reference = {"id": profile["id"], "name": profile["name"]}
    if profile.get("github"):
        reference["github"] = profile["github"]
    return reference


def enrich_example(example: dict, registry: AuthorRegistry) -> dict:
    """Return generated example metadata with resolved authors and licence."""

    enriched = copy.deepcopy(example)
    resolved = []
    seen_ids = set()
    for name in example_author_names(example, registry):
        profile = registry.resolve(name)
        if profile["id"] in seen_ids:
            continue
        seen_ids.add(profile["id"])
        resolved.append(_public_author_reference(profile))

    enriched["authors"] = resolved
    enriched["author"] = ", ".join(profile["name"] for profile in resolved)

    license_value = enriched.get("license")
    if license_value is None or (isinstance(license_value, str) and not license_value.strip()):
        enriched["license"] = DEFAULT_EXAMPLE_LICENSE
        enriched["license_url"] = DEFAULT_EXAMPLE_LICENSE_URL
    else:
        enriched["license"] = _clean_name(license_value, "example license")
        if enriched["license"] == DEFAULT_EXAMPLE_LICENSE:
            enriched["license_url"] = DEFAULT_EXAMPLE_LICENSE_URL
        else:
            enriched.pop("license_url", None)
    return enriched


def _avatar_url(profile: dict) -> str:
    if profile.get("avatar"):
        return profile["avatar"]
    if profile.get("github"):
        return f"https://github.com/{profile['github']}.png?size=240"
    return DEFAULT_AVATAR


def _read_json(path: Path, default):
    if not path.is_file():
        return copy.deepcopy(default)
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False),
        encoding="utf-8",
    )


def _replace_frontmatter(path: Path, data: dict) -> None:
    if not path.is_file():
        return
    parts = path.read_text(encoding="utf-8").split("---", maxsplit=2)
    if len(parts) != 3:
        return
    content = parts[2].strip()
    frontmatter = yaml.dump(data, allow_unicode=True, width=10_000, default_flow_style=False).strip()
    rendered = f"---\n{frontmatter}\n---\n\n"
    if content:
        rendered += f"{content}\n"
    path.write_text(rendered, encoding="utf-8")


def _author_page(author: dict, page_id: str, compatibility: bool = False) -> str:
    author_data_id = page_id if compatibility else author["id"]
    lines = [
        "---",
        "layout: author",
        f"author: {author_data_id}",
        f"title: {json.dumps(author['name'], ensure_ascii=False)}",
        f"permalink: /authors/{page_id}/",
    ]
    if compatibility:
        lines.extend(
            [
                "pagefind_exclude: true",
                f"canonical: /authors/{author['id']}/",
            ]
        )
    lines.extend(["---", ""])
    return "\n".join(lines)


def generate_author_outputs(root: os.PathLike | str = ".", sync_example_pages: bool = True) -> list[dict]:
    """Aggregate Asset Portal and Examples contributors and write Jekyll data.

    This pass is intentionally safe to run after either importer.  It consumes
    whichever generated asset and example data currently exists, enriches both
    sources, and then replaces the author collection as one coherent output.
    """

    root = Path(root)
    registry = AuthorRegistry.load(root / "author_profiles")
    authors: dict[str, dict] = {}
    compatibility_names: dict[str, set[str]] = {}
    seen_assets: dict[str, set[str]] = {}
    seen_examples: dict[str, set[str]] = {}

    def ensure_author(profile: dict) -> dict:
        author = authors.get(profile["id"])
        if author is None:
            author = copy.deepcopy(profile)
            author["avatar_url"] = _avatar_url(profile)
            author["assets"] = []
            author["examples"] = []
            authors[profile["id"]] = author
            compatibility_names[profile["id"]] = set(profile.get("aliases", []))
            seen_assets[profile["id"]] = set()
            seen_examples[profile["id"]] = set()
        return author

    assets_dir = root / "_data" / "assets"
    if assets_dir.is_dir():
        for asset_path in sorted(assets_dir.glob("*.json")):
            asset = _read_json(asset_path, {})
            raw_name = _clean_name(asset.get("author"))
            profile = registry.resolve(raw_name)
            author = ensure_author(profile)
            # Asset Portal author ids have historically been the MD5 of the
            # exact upstream author string. Keep that value stable even when
            # the registry resolves the name to a richer canonical profile.
            asset["author_id"] = canonical_author_id(raw_name)
            _write_json(asset_path, asset)
            if asset_path.stem not in seen_assets[profile["id"]]:
                author["assets"].append(
                    {"id": asset_path.stem, "stars": asset.get("stars") or 0}
                )
                seen_assets[profile["id"]].add(asset_path.stem)
            if raw_name != profile["name"]:
                compatibility_names[profile["id"]].add(raw_name)

    examples_path = root / "_data" / "examplesindex.json"
    examples = _read_json(examples_path, [])
    enriched_examples = []
    for example in examples:
        raw_names = example_author_names(example, registry)
        enriched = enrich_example(example, registry)
        enriched_examples.append(enriched)
        for raw_name in raw_names:
            profile = registry.resolve(raw_name)
            author = ensure_author(profile)
            path = enriched.get("path")
            if path and path not in seen_examples[profile["id"]]:
                image = ""
                if enriched.get("thumbnail"):
                    image = f"/examples/{path}/{enriched['thumbnail']}"
                author["examples"].append(
                    {
                        "author": enriched["author"],
                        "brief": enriched.get("brief") or "",
                        "category": enriched.get("category") or "",
                        "image": image,
                        "path": path,
                        "title": enriched.get("title") or path,
                    }
                )
                seen_examples[profile["id"]].add(path)
            if raw_name != profile["name"]:
                compatibility_names[profile["id"]].add(raw_name)

        if sync_example_pages and enriched.get("path"):
            _replace_frontmatter(root / "examples" / enriched["path"] / "index.md", enriched)

    if examples_path.is_file() or enriched_examples:
        _write_json(examples_path, enriched_examples)

    author_list = sorted(authors.values(), key=lambda author: author["name"].casefold())
    for author in author_list:
        author["assets"].sort(key=lambda item: item["id"].casefold())
        author["examples"].sort(key=lambda item: item["path"].casefold())

    author_data_dir = root / "_data" / "authors"
    author_collection_dir = root / "authors"
    for directory in (author_data_dir, author_collection_dir):
        if directory.exists():
            shutil.rmtree(directory)
        directory.mkdir(parents=True)

    for author in author_list:
        _write_json(author_data_dir / f"{author['id']}.json", author)
        (author_collection_dir / f"{author['id']}.md").write_text(
            _author_page(author, author["id"]), encoding="utf-8"
        )
        for alias in sorted(compatibility_names[author["id"]], key=str.casefold):
            alias_id = canonical_author_id(alias)
            if alias_id == author["id"]:
                continue
            compatibility_author = copy.deepcopy(author)
            compatibility_author["id"] = alias_id
            _write_json(author_data_dir / f"{alias_id}.json", compatibility_author)
            (author_collection_dir / f"{alias_id}.md").write_text(
                _author_page(author, alias_id, compatibility=True), encoding="utf-8"
            )

    _write_json(root / "_data" / "authorindex.json", author_list)
    return author_list
