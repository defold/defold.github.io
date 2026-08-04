# Author profiles

`profiles.json` is the hand-maintained identity registry for Asset Portal and Examples contributors. It is website source, not generated `_data`. Generated author pages and `_data/authors/` are rebuilt by `scripts.author_profiles.generate_author_outputs()` after either import in `update.py`.

Each profile requires a canonical `name` and may define:

- `github`: a GitHub username, used for identity matching, the profile link, and the default avatar.
- `aliases`: legacy display names and capitalization variants. Alias hash pages are generated for URL compatibility.
- `bio`: a short biography of up to 280 characters.
- `avatar`: an HTTPS URL or a site-root-relative image path.
- `links`: HTTPS `website`, `x`, `bluesky`, `mastodon`, or `linkedin` links.
- `support`: up to three allowlisted `github_sponsors`, `ko_fi`, `patreon`, `buy_me_a_coffee`, or `paypal` actions.

Names resolve case-insensitively against canonical names, GitHub usernames, and aliases. Contributors missing from the registry still receive a generated minimal profile, but current source contributors should normally be registered so display names and URLs remain deliberate.

Asset Portal `author_id` values remain the MD5 of the exact upstream `author` string. Resolving an alias enriches and combines the profile without changing that imported id; the legacy hash receives a compatibility data record and page pointing at the canonical profile URL.
