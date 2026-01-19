import html
import json
import os
import re
import shutil


LLMS_DIR = "_llms"
LLMS_OUTPUT_DIR = "llms"
LLMS_MANUALS_DIR = os.path.join(LLMS_OUTPUT_DIR, "manuals")
LLMS_APIS_DIR = os.path.join(LLMS_OUTPUT_DIR, "apis")
LLMS_EXAMPLES_DIR = os.path.join(LLMS_OUTPUT_DIR, "examples")
LLMS_MANUALS_FILE = "llms-manuals.txt"
LLMS_APIS_FILE = "llms-apis.txt"
LLMS_EXAMPLES_FILE = "llms-examples.txt"
LLMS_FULL_FILE = "llms-full.txt"


def rmtree(dir):
    if os.path.exists(dir):
        shutil.rmtree(dir)


def list_files(dir, ext, sort = False):
    files = []
    for file in os.listdir(dir):
        if file.endswith(ext):
            files.append(file)
    if sort:
        files.sort()
    return files


def read_as_string(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


def read_as_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)


def write_as_string(filename, s):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(s)


def add_anchor_to_first_heading(contents, anchor, prefix):
    lines = contents.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            lines[i] = "{} {{#{}:{}}}".format(line, prefix, anchor)
            break
    return "\n".join(lines)


def build_llms_manuals_content(index):
    llms_content = []

    # Add headline and intro
    llms_content.append("# Defold Documentation\n")
    llms_content.append("> Defold is a free game engine with free source code access. It's designed for creating 2D and 3D games across multiple platforms, including mobile, desktop, web, and consoles.\n")

    llms_content.append("This document contains [Defold's official documentation](https://defold.com/manuals/) in a single-file easy-to-search form.")
    llms_content.append("If you find any issues, please report them [as a GitHub issue](https://github.com/defold/doc/issues), and contributions are very welcome in the form of [pull requests](https://github.com/defold/doc/pulls).\n")

    # Add sections from index
    manuals_content = []
    manuals_included = {}
    llms_content.append("## Manuals\n")
    for section in index["navigation"]["manuals"]:
        section_title = section["name"]
        llms_content.append(f"### {section_title}\n")
        for item in section["items"]:
            path = item["path"]
            title = item["name"]
            path_no_anchors = re.sub(r"(/)?#.+", "", path)
            if manuals_included.get(path_no_anchors):
                print(f" -> already included {path}")
                anchor = manuals_included.get(path_no_anchors)
                llms_content.append(f"- [{title}](#{anchor})")
            else:
                if not os.path.exists(LLMS_DIR + path_no_anchors + ".md"):
                    url = path if "https://" in path else "https://defold.com" + path
                    llms_content.append(f"- [{title}]({url})")
                    print(f" -> skipping {path}")
                else:
                    anchor = path_no_anchors.replace("/", ":").lstrip(":")
                    manuals_included[path_no_anchors] = anchor
                    llms_content.append(f"- [{title}](#{anchor})")
                    contents = read_as_string(LLMS_DIR + path_no_anchors + ".md")
                    contents = clean_markdown(contents)
                    manuals_content.append(f"<!-- {path} -->\n")
                    manuals_content.append(contents)
                    manuals_content.append("")
        llms_content.append("")
    llms_content.append("")

    llms_content.extend(manuals_content)

    return llms_content


def generate_llms_manuals(index):
    manuals_index = []
    manuals_included = {}

    os.makedirs(LLMS_OUTPUT_DIR, exist_ok=True)
    rmtree(LLMS_MANUALS_DIR)
    os.makedirs(LLMS_MANUALS_DIR, exist_ok=True)

    manuals_index.append("# Defold Manuals\n")
    manuals_index.append("These are per-manual files generated for LLM usage.\n")

    for section in index["navigation"]["manuals"]:
        section_title = section["name"]
        manuals_index.append(f"## {section_title}\n")
        for item in section["items"]:
            path = item["path"]
            title = item["name"]
            path_no_anchors = re.sub(r"(/)?#.+", "", path)
            llms_source = LLMS_DIR + path_no_anchors + ".md"
            if os.path.exists(llms_source):
                manual_rel_path = path_no_anchors.lstrip("/")
                if manual_rel_path.startswith("manuals/"):
                    manual_rel_path = manual_rel_path[len("manuals/"):]
                manual_output = os.path.join(LLMS_MANUALS_DIR, manual_rel_path + ".md")
                if not manuals_included.get(path_no_anchors):
                    manuals_included[path_no_anchors] = manual_rel_path
                    os.makedirs(os.path.dirname(manual_output), exist_ok=True)
                    contents = read_as_string(llms_source)
                    contents = clean_markdown(contents)
                    contents = re.sub(r"\(#manuals:([^)]+)\)", lambda m: f"({m.group(1).replace(':', '/')}.md)", contents)
                    write_as_string(manual_output, contents)
                manuals_index.append(f"- [{title}](manuals/{manual_rel_path}.md)")
            else:
                url = path if "https://" in path else "https://defold.com" + path
                manuals_index.append(f"- [{title}]({url})")
        manuals_index.append("")

    write_as_string(os.path.join(LLMS_OUTPUT_DIR, "manuals.md"), "\n".join(manuals_index))
    write_as_string(LLMS_MANUALS_FILE, "\n".join(build_llms_manuals_content(index)))
    generate_llms_full()


def format_api_types(types):
    if not types:
        return ""
    if isinstance(types, list):
        return " | ".join([str(t) for t in types if t])
    return str(types)


def api_summary(info):
    summary = info.get("description") or info.get("brief") or ""
    summary = re.sub(r"\s+", " ", summary).strip()
    dot_index = summary.find(".")
    if dot_index > 0:
        summary = summary[:dot_index].strip()
    return summary


def strip_markdown_images(text):
    if not text:
        return ""
    lines = text.splitlines()
    output = []
    in_code = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            output.append(line)
            continue
        if in_code:
            output.append(line)
            continue
        line = re.sub(r"<img[^>]*>", "", line, flags=re.IGNORECASE)
        line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", line)
        line = re.sub(r"!\[[^\]]*\]\[[^\]]*\]", "", line)
        output.append(line)
    return "\n".join(output)


def apply_outside_code(text, transform):
    if not text:
        return ""
    lines = text.splitlines()
    output = []
    buffer = []
    in_code = False
    for line in lines:
        if line.strip().startswith("```"):
            if buffer:
                output.extend(transform("\n".join(buffer)).splitlines())
                buffer = []
            output.append(line)
            in_code = not in_code
            continue
        if in_code:
            output.append(line)
        else:
            buffer.append(line)
    if buffer:
        output.extend(transform("\n".join(buffer)).splitlines())
    return "\n".join(output)


def strip_inline_html(text):
    if not text:
        return ""

    def transform(chunk):
        chunk = re.sub(r"<\s*kbd\s*>(.*?)</\s*kbd\s*>", r"`\1`", chunk, flags=re.IGNORECASE | re.DOTALL)
        chunk = re.sub(r"<\s*code\s*>(.*?)</\s*code\s*>", r"`\1`", chunk, flags=re.IGNORECASE | re.DOTALL)
        chunk = re.sub(r"<\s*br\s*/?\s*>", "\n", chunk, flags=re.IGNORECASE)
        chunk = re.sub(r"</\s*p\s*>", "\n", chunk, flags=re.IGNORECASE)
        chunk = re.sub(r"<\s*p\s*>", "", chunk, flags=re.IGNORECASE)
        chunk = re.sub(r"</?[^>]+>", "", chunk)
        return chunk

    return apply_outside_code(text, transform)


def collapse_blank_lines(text):
    if not text:
        return ""
    lines = text.splitlines()
    output = []
    in_code = False
    blank_pending = False
    for line in lines:
        stripped = line.rstrip()
        if stripped.strip().startswith("```"):
            in_code = not in_code
            output.append(stripped)
            blank_pending = False
            continue
        if in_code:
            output.append(line.rstrip())
            continue
        if stripped.strip() == "":
            if not blank_pending:
                output.append("")
                blank_pending = True
            continue
        blank_pending = False
        output.append(stripped)
    while output and output[-1] == "":
        output.pop()
    return "\n".join(output)


def clean_markdown(text):
    text = strip_markdown_images(text)
    text = strip_inline_html(text)
    text = collapse_blank_lines(text)
    return text


def collect_llms_api_entries():
    cpp_entries = []
    lua_entries = []
    extension_entries = []

    ref_root = os.path.join("_data", "ref", "stable")
    if os.path.isdir(ref_root):
        for filename in list_files(ref_root, ".json", sort = True):
            api = read_as_json(os.path.join(ref_root, filename))
            info = api.get("info", {})
            language = info.get("language")
            if language not in ("C++", "Lua"):
                continue
            output_name = os.path.splitext(filename)[0]
            label = info.get("namespace") or info.get("name") or output_name
            if info.get("name") and info.get("namespace") and info.get("name") != info.get("namespace"):
                label = "{} ({})".format(info.get("namespace"), info.get("name"))

            entry = {
                "label": label,
                "output_name": output_name,
                "summary": api_summary(info),
                "info": info,
                "elements": api.get("elements", []),
            }

            if language == "C++":
                cpp_entries.append(entry)
            else:
                lua_entries.append(entry)

    extensions_root = os.path.join("_data", "extensions")
    if os.path.isdir(extensions_root):
        for filename in list_files(extensions_root, ".json", sort = True):
            api = read_as_json(os.path.join(extensions_root, filename))
            info = api.get("info", {})
            output_name = os.path.splitext(filename)[0]
            label = info.get("namespace") or info.get("name") or output_name
            if info.get("name") and info.get("namespace") and info.get("name") != info.get("namespace"):
                label = "{} ({})".format(info.get("namespace"), info.get("name"))

            extension_entries.append({
                "label": label,
                "output_name": output_name,
                "summary": api_summary(info),
                "info": info,
                "elements": api.get("elements", []),
            })

    return cpp_entries, lua_entries, extension_entries


def strip_html(text):
    if not text:
        return ""
    text = html.unescape(text)
    text = re.sub(r"<div[^>]*class=[\"']codehilite[\"'][^>]*>\s*<pre[^>]*>\s*<span[^>]*></span>\s*<code[^>]*>", "```\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<pre[^>]*>\s*<code[^>]*>", "```\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</code>\s*</pre>\s*</div>", "\n```", text, flags=re.IGNORECASE)
    text = re.sub(r"</code>\s*</pre>", "\n```", text, flags=re.IGNORECASE)
    text = re.sub(r"</?span[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"<br\\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"</p>\\s*<p[^>]*>", "\n\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def format_api_params(params, indent = 0):
    lines = []
    for p in params:
        name = p.get("name", "")
        types = format_api_types(p.get("types") or p.get("type"))
        doc = p.get("doc") or p.get("description") or ""
        optional = str(p.get("is_optional", "")).lower() == "true"

        label = "`{}`".format(name or "param")
        if types:
            label = "{} ({})".format(label, types)
        if optional:
            label = "{} (optional)".format(label)

        if doc:
            lines.append("{}- {} - {}".format(" " * indent, label, doc))
        else:
            lines.append("{}- {}".format(" " * indent, label))

        sub = p.get("parameters") or []
        if sub:
            lines.extend(format_api_params(sub, indent = indent + 2))
    return lines


def format_api_members(members, indent = 0):
    lines = []
    for m in members:
        name = m.get("name", "")
        mtype = m.get("type") or ""
        doc = m.get("doc") or m.get("description") or ""

        label = "`{}`".format(name or "member")
        if mtype:
            label = "{} ({})".format(label, mtype)

        if doc:
            lines.append("{}- {} - {}".format(" " * indent, label, doc))
        else:
            lines.append("{}- {}".format(" " * indent, label))
    return lines


def format_api_returnvalues(returns):
    lines = []
    for r in returns:
        name = r.get("name", "")
        types = format_api_types(r.get("types"))
        doc = r.get("doc") or r.get("description") or ""

        label = "`{}`".format(name or "return")
        if types:
            label = "{} ({})".format(label, types)

        if doc:
            lines.append("- {} - {}".format(label, doc))
        else:
            lines.append("- {}".format(label))
    return lines


def render_api_markdown(info, elements):
    lines = []
    title = info.get("name") or info.get("namespace") or "API"
    lines.append("# {}".format(title))
    lines.append("")

    namespace = info.get("namespace")
    if namespace:
        lines.append("**Namespace:** `{}`".format(namespace))
    language = info.get("language")
    if language:
        lines.append("**Language:** {}".format(language))
    api_type = info.get("type")
    if api_type:
        lines.append("**Type:** {}".format(api_type))
    file_name = info.get("file")
    if file_name:
        lines.append("**File:** `{}`".format(file_name))
    source = info.get("path")
    if source:
        lines.append("**Source:** `{}`".format(source))
    include = info.get("include")
    if include:
        lines.append("**Include:** `{}`".format(include))

    description = collapse_blank_lines(strip_markdown_images(strip_html(info.get("description"))))
    if description:
        lines.append("")
        lines.append(description)

    notes = info.get("notes") or []
    if notes:
        lines.append("")
        lines.append("## Notes")
        lines.append("")
        lines.extend(["- {}".format(n) for n in notes])

    if elements:
        lines.append("")
        lines.append("## API")
        lines.append("")
        for el in elements:
            name = el.get("name", "")
            lines.append("### {}".format(name))

            el_type = el.get("type")
            if el_type:
                lines.append("*Type:* {}".format(el_type))

            desc = collapse_blank_lines(strip_markdown_images(strip_html(el.get("description") or el.get("brief"))))
            if desc:
                lines.append(desc)

            el_notes = el.get("notes") or []
            if el_notes:
                lines.append("")
                lines.append("**Notes**")
                lines.append("")
                lines.extend(["- {}".format(n) for n in el_notes])

            tparams = el.get("tparams") or []
            if tparams:
                lines.append("")
                lines.append("**Template Parameters**")
                lines.append("")
                lines.extend(format_api_members(tparams))

            params = el.get("parameters") or []
            if params:
                lines.append("")
                lines.append("**Parameters**")
                lines.append("")
                lines.extend(format_api_params(params))

            members = el.get("members") or []
            if members:
                lines.append("")
                lines.append("**Members**")
                lines.append("")
                lines.extend(format_api_members(members))

            returns = el.get("returnvalues") or []
            if returns:
                lines.append("")
                lines.append("**Returns**")
                lines.append("")
                lines.extend(format_api_returnvalues(returns))

            error = el.get("error")
            if error:
                lines.append("")
                lines.append("**Errors**")
                lines.append("")
                lines.append(error)

            replaces = el.get("replaces")
            if replaces:
                lines.append("")
                lines.append("**Replaces:** {}".format(replaces))

            examples = collapse_blank_lines(strip_markdown_images(strip_html(el.get("examples"))))
            if examples:
                lines.append("")
                lines.append("**Examples**")
                lines.append("")
                lines.append(examples)

            lines.append("")

    return collapse_blank_lines("\n".join(lines)).rstrip() + "\n"


def build_llms_apis_content(cpp_entries, lua_entries, extension_entries):
    apis_content = []

    apis_content.append("# Defold API Reference\n")
    apis_content.append("This document contains the Defold API reference, grouped by language.\n")

    apis_content.append("## C++ APIs\n")
    for entry in cpp_entries:
        if entry["summary"]:
            apis_content.append("- [{}](#apis:{}) - {}".format(entry["label"], entry["output_name"], entry["summary"]))
        else:
            apis_content.append("- [{}](#apis:{})".format(entry["label"], entry["output_name"]))
    apis_content.append("")

    apis_content.append("## Lua APIs\n")
    for entry in lua_entries:
        if entry["summary"]:
            apis_content.append("- [{}](#apis:{}) - {}".format(entry["label"], entry["output_name"], entry["summary"]))
        else:
            apis_content.append("- [{}](#apis:{})".format(entry["label"], entry["output_name"]))
    apis_content.append("")

    apis_content.append("## Extension APIs\n")
    for entry in extension_entries:
        if entry["summary"]:
            apis_content.append("- [{}](#apis:{}) - {}".format(entry["label"], entry["output_name"], entry["summary"]))
        else:
            apis_content.append("- [{}](#apis:{})".format(entry["label"], entry["output_name"]))
    apis_content.append("")

    for entry in cpp_entries + lua_entries + extension_entries:
        apis_content.append("<!-- {} -->\n".format(entry["output_name"]))
        api_md = render_api_markdown(entry["info"], entry["elements"])
        apis_content.append(add_anchor_to_first_heading(api_md, entry["output_name"], "apis"))
        apis_content.append("")

    return apis_content


def split_llms_content(content):
    if not content:
        return "", ""
    match = re.search(r"(?m)^<!--", content)
    if not match:
        return content.strip(), ""
    header = content[:match.start()].strip()
    body = content[match.start():].strip()
    return header, body


def generate_llms_full():
    manuals_content = read_as_string(LLMS_MANUALS_FILE) if os.path.exists(LLMS_MANUALS_FILE) else ""
    apis_content = read_as_string(LLMS_APIS_FILE) if os.path.exists(LLMS_APIS_FILE) else ""
    examples_content = read_as_string(LLMS_EXAMPLES_FILE) if os.path.exists(LLMS_EXAMPLES_FILE) else ""

    manuals_header, manuals_body = split_llms_content(manuals_content)
    apis_header, apis_body = split_llms_content(apis_content)
    examples_header, examples_body = split_llms_content(examples_content)

    parts = []
    if manuals_header:
        parts.append(manuals_header)
    if apis_header:
        parts.append(apis_header)
    if examples_header:
        parts.append(examples_header)
    if manuals_body:
        parts.append(manuals_body)
    if apis_body:
        parts.append(apis_body)
    if examples_body:
        parts.append(examples_body)

    if not parts:
        return
    with open(LLMS_FULL_FILE, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts))
        f.write("\n")


def generate_llms_apis():
    apis_index = []
    cpp_entries, lua_entries, extension_entries = collect_llms_api_entries()

    os.makedirs(LLMS_OUTPUT_DIR, exist_ok=True)
    rmtree(LLMS_APIS_DIR)
    os.makedirs(LLMS_APIS_DIR, exist_ok=True)

    apis_index.append("# Defold API Reference\n")
    apis_index.append("These are per-namespace API reference files generated for LLM usage.\n")

    for entry in cpp_entries + lua_entries + extension_entries:
        output_path = os.path.join(LLMS_APIS_DIR, entry["output_name"] + ".md")
        write_as_string(output_path, render_api_markdown(entry["info"], entry["elements"]))

    apis_index.append("## C++ APIs\n")
    for entry in cpp_entries:
        label = entry["label"]
        output_name = entry["output_name"]
        summary = entry["summary"]
        if summary:
            apis_index.append("- [{}](apis/{}.md) - {}".format(label, output_name, summary))
        else:
            apis_index.append("- [{}](apis/{}.md)".format(label, output_name))
    apis_index.append("")

    apis_index.append("## Lua APIs\n")
    for entry in lua_entries:
        label = entry["label"]
        output_name = entry["output_name"]
        summary = entry["summary"]
        if summary:
            apis_index.append("- [{}](apis/{}.md) - {}".format(label, output_name, summary))
        else:
            apis_index.append("- [{}](apis/{}.md)".format(label, output_name))
    apis_index.append("")

    apis_index.append("## Extension APIs\n")
    for entry in extension_entries:
        label = entry["label"]
        output_name = entry["output_name"]
        summary = entry["summary"]
        if summary:
            apis_index.append("- [{}](apis/{}.md) - {}".format(label, output_name, summary))
        else:
            apis_index.append("- [{}](apis/{}.md)".format(label, output_name))
    apis_index.append("")

    write_as_string(os.path.join(LLMS_OUTPUT_DIR, "apis.md"), "\n".join(apis_index))
    write_as_string(LLMS_APIS_FILE, "\n".join(build_llms_apis_content(cpp_entries, lua_entries, extension_entries)))
    generate_llms_full()


def example_summary(entry):
    summary = entry.get("brief") or ""
    summary = re.sub(r"\s+", " ", summary).strip()
    dot_index = summary.find(".")
    if dot_index > 0:
        summary = summary[:dot_index].strip()
    return summary


def rewrite_example_links(content, example_path):
    if not content:
        return ""
    base_url = "https://defold.com/examples/{}".format(example_path)

    def rewrite_image(match):
        alt = match.group(1)
        url = match.group(2)
        if re.match(r"^(https?://|/|#|data:)", url):
            return match.group(0)
        return "![{}]({}/{})".format(alt, base_url, url.lstrip("./"))

    def rewrite_link(match):
        label = match.group(1)
        url = match.group(2)
        if re.match(r"^(https?://|/|#|data:)", url):
            return match.group(0)
        return "[{}]({}/{})".format(label, base_url, url.lstrip("./"))

    content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", rewrite_image, content)
    content = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", rewrite_link, content)
    return content


def render_example_markdown(entry, content):
    lines = []
    title = entry.get("title") or entry.get("path") or "Example"
    lines.append("# {}".format(title))
    lines.append("")
    summary = entry.get("brief")
    if summary:
        lines.append(summary)
        lines.append("")
    path = entry.get("path")
    if path:
        source_url = "https://github.com/defold/examples/tree/master/{}".format(path)
        lines.append("Source: [{}]({})".format(source_url, source_url))
        lines.append("")
    if content:
        lines.append(content.strip())
        lines.append("")
    scripts = entry.get("llms_scripts") or []
    if scripts:
        lines.append("## Scripts")
        lines.append("")
        for script in scripts:
            name = script.get("name") or "script"
            language = script.get("language") or ""
            script_body = script.get("content") or ""
            lines.append("### {}".format(name))
            lines.append("")
            if language:
                lines.append("```{}".format(language))
            else:
                lines.append("```")
            lines.append(script_body.rstrip())
            lines.append("```")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generate_llms_examples():
    index_file = os.path.join("_data", "examplesindex.json")
    if not os.path.exists(index_file):
        return

    examples = read_as_json(index_file)
    if not examples:
        return

    os.makedirs(LLMS_OUTPUT_DIR, exist_ok=True)
    rmtree(LLMS_EXAMPLES_DIR)
    os.makedirs(LLMS_EXAMPLES_DIR, exist_ok=True)

    examples_index = []
    examples_index.append("# Defold Examples\n")
    examples_index.append("These are per-example files generated for LLM usage.\n")

    examples_content = []
    examples_content.append("# Defold Examples\n")
    examples_content.append("This document contains Defold examples grouped by category.\n")

    categories = {}
    for entry in examples:
        category = entry.get("category") or "misc"
        categories.setdefault(category, []).append(entry)

    for category in sorted(categories.keys()):
        items = sorted(categories[category], key=lambda x: x.get("title", "").lower())
        examples_index.append("## {}\n".format(category.capitalize()))
        examples_content.append("## {}\n".format(category.capitalize()))
        for entry in items:
            path = entry.get("path")
            title = entry.get("title") or path
            summary = example_summary(entry)
            output_rel = "{}.md".format(path)
            output_path = os.path.join(LLMS_EXAMPLES_DIR, output_rel)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)

            source_path = os.path.join("examples", path, "index.md")
            content = read_as_string(source_path) if os.path.exists(source_path) else ""
            content = re.sub(r"---\n(.*?)---\n+", "", content, flags=re.DOTALL)
            content = rewrite_example_links(content, path)
            content = clean_markdown(content)
            entry["llms_scripts"] = []
            scripts_value = entry.get("scripts") or ""
            if isinstance(scripts_value, list):
                scripts_list = scripts_value
            else:
                scripts_list = [s.strip() for s in str(scripts_value).split(",") if s.strip()]
            for script_name in scripts_list:
                include_name = script_name
                include_name = include_name.replace(".script", "_script.md")
                include_name = include_name.replace(".gui_script", "_gui_script.md")
                include_name = include_name.replace(".vp", "_vp.md")
                include_name = include_name.replace(".fp", "_fp.md")
                include_path = os.path.join("_includes", "examples", path, include_name)
                if not os.path.exists(include_path):
                    continue
                if script_name.endswith((".script", ".gui_script")):
                    language = "lua"
                elif script_name.endswith((".vp", ".fp")):
                    language = "glsl"
                else:
                    language = ""
                entry["llms_scripts"].append({
                    "name": script_name,
                    "language": language,
                    "content": read_as_string(include_path),
                })

            write_as_string(output_path, render_example_markdown(entry, content))

            if summary:
                examples_index.append("- [{}](examples/{}) - {}".format(title, output_rel, summary))
                examples_content.append("- [{}](#examples:{}) - {}".format(title, path.replace("/", ":"), summary))
            else:
                examples_index.append("- [{}](examples/{})".format(title, output_rel))
                examples_content.append("- [{}](#examples:{})".format(title, path.replace("/", ":")))
        examples_index.append("")
        examples_content.append("")

    for category in sorted(categories.keys()):
        items = sorted(categories[category], key=lambda x: x.get("title", "").lower())
        for entry in items:
            path = entry.get("path")
            output_rel = "{}.md".format(path)
            output_path = os.path.join(LLMS_EXAMPLES_DIR, output_rel)
            if not os.path.exists(output_path):
                continue
            examples_content.append("<!-- {} -->\n".format(path))
            example_md = read_as_string(output_path)
            examples_content.append(add_anchor_to_first_heading(example_md, path.replace("/", ":"), "examples"))
            examples_content.append("")

    write_as_string(os.path.join(LLMS_OUTPUT_DIR, "examples.md"), "\n".join(examples_index))
    write_as_string(LLMS_EXAMPLES_FILE, "\n".join(examples_content))
    generate_llms_full()


# replace the relative links to anchors
def path_to_manuals_anchor(match):
    path = match.group(2)
    anchor = path.replace("/", ":").lstrip(":")
    anchor = re.sub(r":#.*", "", anchor) # temporarily strip in-documentanchors
    return f"(#manuals:{anchor})"
