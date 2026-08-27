import html
import re
from urllib.parse import quote


SUPPORTED_FORMAT_VERSIONS = (1, 2)

_LUA_TYPE_ELEMENT_TYPES = frozenset((
    "CLASS", "ENUM", "MESSAGE", "STRUCT", "TYPEDEF",
))
_LUA_MANUAL_TYPE_HREFS = {
    "any": "../../../manuals/lua/#variables-and-data-types",
    "boolean": "../../../manuals/lua/#variables-and-data-types",
    "function": "../../../manuals/lua/#variables-and-data-types",
    "integer": "../../../manuals/lua/#variables-and-data-types",
    "nil": "../../../manuals/lua/#variables-and-data-types",
    "number": "../../../manuals/lua/#variables-and-data-types",
    "object": "../../../manuals/lua/#variables-and-data-types",
    "string": "../../../manuals/lua/#variables-and-data-types",
    "table": "../../../manuals/lua/#variables-and-data-types",
    "thread": "../coroutine-lua/",
    "userdata": "../../../manuals/lua/#variables-and-data-types",
}
_LUA_TYPE_IDENTIFIER_RE = re.compile(
    r"[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*")
_LUA_TYPE_SPAN_RE = re.compile(
    r'<span class="type">((?:(?!</span>).)*?)</span>',
    re.DOTALL)
_LUA_TYPE_DEFINITION_RE = re.compile(
    r'<dt><code>([^<]*)</code></dt>\s*'
    r'<dd>\s*<span class="type">((?:(?!</span>).)*?)</span>(\]*)\s*'
    r'((?:(?!<dl\b|</dl>|<dt\b|<dd\b).)*?)\s*</dd>',
    re.DOTALL)
_LUA_TYPE_DELIMITERS = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}


def format_version(api, source="reference document"):
    version = api.get("format_version", 1)
    if isinstance(version, bool) or not isinstance(version, int):
        raise ValueError(
            "%s has invalid format_version %r; expected an integer"
            % (source, version))
    if version not in SUPPORTED_FORMAT_VERSIONS:
        raise ValueError(
            "%s uses unsupported format_version %d; supported versions are %s"
            % (source, version, ", ".join(map(str, SUPPORTED_FORMAT_VERSIONS))))
    return version


def require_matching_format_versions(existing, incoming, namespace, source):
    existing_version = format_version(existing, namespace)
    incoming_version = format_version(incoming, source)
    if existing_version != incoming_version:
        raise ValueError(
            "%s mixes reference-document format versions %d and %d"
            % (namespace, existing_version, incoming_version))


def lua_type_targets(namespaces):
    """Index documented Lua elements that can be type-link targets."""
    targets = {}
    for page, api in namespaces.items():
        if api.get("info", {}).get("api_language") != "Lua":
            continue
        if format_version(api) != 2:
            continue
        for element in api.get("elements", []):
            name = element.get("name")
            if not name:
                continue
            priority = 0 if element.get("type") in _LUA_TYPE_ELEMENT_TYPES else 1
            target = (priority, page, name)
            candidates = targets.setdefault(name, [])
            if target not in candidates:
                candidates.append(target)
            if element.get("type") == "MESSAGE":
                namespace = api.get("info", {}).get("namespace")
                if namespace:
                    message_type = "message.%s.%s" % (
                        namespace, name.rsplit(".", 1)[-1])
                    message_candidates = targets.setdefault(message_type, [])
                    if target not in message_candidates:
                        message_candidates.append(target)
    return targets


def _lua_type_href(name, current_page, targets):
    manual_href = _LUA_MANUAL_TYPE_HREFS.get(name)
    if manual_href:
        return manual_href

    candidates = targets.get(name, ())
    if not candidates:
        return None

    priority = min(candidate[0] for candidate in candidates)
    candidates = {
        (page, anchor)
        for candidate_priority, page, anchor in candidates
        if candidate_priority == priority
    }
    local_candidates = {
        candidate for candidate in candidates if candidate[0] == current_page
    }
    if len(local_candidates) == 1:
        page, anchor = next(iter(local_candidates))
    elif len(candidates) == 1:
        page, anchor = next(iter(candidates))
    else:
        return None

    anchor = quote(anchor, safe="._-")
    if page == current_page:
        return "#" + anchor
    return "../{}/#{}".format(quote(page, safe="._-"), anchor)


def _quoted_characters(value):
    quoted = [False] * len(value)
    quote_character = None
    escaped = False
    for index, character in enumerate(value):
        if quote_character:
            quoted[index] = True
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote_character:
                quote_character = None
        elif character in ("\"", "'"):
            quoted[index] = True
            quote_character = character
    return quoted


def _is_type_label(value, identifier_end):
    index = identifier_end
    while index < len(value) and value[index].isspace():
        index += 1
    if index < len(value) and value[index] == "?":
        index += 1
        while index < len(value) and value[index].isspace():
            index += 1
    return index < len(value) and value[index] == ":"


def link_lua_type(value, current_page, targets):
    """Render a LuaLS type expression with links to documented types."""
    value = value or ""
    quoted = _quoted_characters(value)
    parts = []
    cursor = 0
    for match in _LUA_TYPE_IDENTIFIER_RE.finditer(value):
        if quoted[match.start()] or _is_type_label(value, match.end()):
            continue
        href = _lua_type_href(match.group(0), current_page, targets)
        if not href:
            continue
        parts.append(html.escape(value[cursor:match.start()], quote=False))
        parts.append('<a href="{}">{}</a>'.format(
            html.escape(href, quote=True),
            html.escape(match.group(0), quote=False)))
        cursor = match.end()
    parts.append(html.escape(value[cursor:], quote=False))
    return "".join(parts)


def _find_lua_type_container_end(value, opening_index):
    stack = []
    quote_character = None
    escaped = False
    for index in range(opening_index, len(value)):
        character = value[index]
        if quote_character:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote_character:
                quote_character = None
        elif character in ("\"", "'"):
            quote_character = character
        elif character in _LUA_TYPE_DELIMITERS:
            stack.append(_LUA_TYPE_DELIMITERS[character])
        elif stack and character == stack[-1]:
            stack.pop()
            if not stack:
                return index
    return None


def _split_lua_type_items(value):
    items = []
    stack = []
    start = 0
    quote_character = None
    escaped = False
    for index, character in enumerate(value):
        if quote_character:
            if escaped:
                escaped = False
            elif character == "\\":
                escaped = True
            elif character == quote_character:
                quote_character = None
        elif character in ("\"", "'"):
            quote_character = character
        elif character in _LUA_TYPE_DELIMITERS:
            stack.append(_LUA_TYPE_DELIMITERS[character])
        elif stack and character == stack[-1]:
            stack.pop()
        elif character == "," and not stack:
            items.append(value[start:index].strip())
            start = index + 1
    items.append(value[start:].strip())
    return [item for item in items if item]


def format_lua_type_for_table(value):
    """Format top-level function arguments or record fields on separate lines."""
    value = (value or "").strip()
    if value.startswith("fun("):
        opening_index = 3
        closing_index = _find_lua_type_container_end(value, opening_index)
        if closing_index is None:
            return value
        items = _split_lua_type_items(value[opening_index + 1:closing_index])
        if not items:
            return "function()" + value[closing_index + 1:]
        return "function(\n\t{}){}".format(
            ",\n\t".join(items), value[closing_index + 1:])

    if value.startswith("{"):
        closing_index = _find_lua_type_container_end(value, 0)
        if closing_index is None:
            return value
        items = _split_lua_type_items(value[1:closing_index])
        if not items:
            return "{}" + value[closing_index + 1:]
        return "{{{}}}{}".format(
            ",\n".join(items), value[closing_index + 1:])

    return value


def _link_lua_type_spans(value, current_page, targets):
    def replace(match):
        linked_type = link_lua_type(
            html.unescape(match.group(1)), current_page, targets)
        if "<a href=" not in linked_type:
            return match.group(0)
        return '<span class="type">{}</span>'.format(linked_type)

    return _LUA_TYPE_SPAN_RE.sub(replace, value or "")


def _format_lua_type_definitions(value):
    def replace(match):
        return (
            '<dt class="api-lua-v2-type-definition"><code>{}:{}</code></dt>\n'
            '<dd>{}</dd>'
        ).format(
            match.group(1).strip(),
            match.group(2).strip() + match.group(3),
            match.group(4).strip())

    return _LUA_TYPE_DEFINITION_RE.sub(replace, value or "")


def _prepare_lua_parameter(parameter, current_page, targets):
    types = parameter.get("types", [])
    parameter["types_html"] = [
        link_lua_type(value, current_page, targets)
        for value in types
    ]
    parameter["types_table_html"] = [
        link_lua_type(
            format_lua_type_for_table(value), current_page, targets)
        for value in types
    ]
    parameter["doc"] = _format_lua_type_definitions(
        _link_lua_type_spans(
            parameter.get("doc", ""), current_page, targets))
    for nested_parameter in parameter.get("parameters", []):
        _prepare_lua_parameter(nested_parameter, current_page, targets)


def _joined_parameter_type(parameters, default):
    value = next(
        (parameter for parameter in parameters if parameter.get("name") == "value"),
        None)
    if not value:
        return default
    return " | ".join(value.get("types") or []) or default


def _qualified_enum_member_name(enum_name, member_name):
    if "." in member_name:
        return member_name
    namespace, separator, _ = enum_name.rpartition(".")
    return "%s.%s" % (namespace, member_name) if separator else member_name


def prepare_lua_v2(api, current_page="", targets=None):
    """Add presentation-oriented fields without changing the source schema."""
    if format_version(api) != 2:
        return api

    targets = targets or {}

    constants = {
        element["name"]: element
        for element in api.get("elements", [])
        if element.get("type") == "CONSTANT"
    }

    for element in api.get("elements", []):
        element_type = element.get("type")
        element["description"] = _link_lua_type_spans(
            element.get("description", ""), current_page, targets)
        for parameter in (
                element.get("parameters", [])
                + element.get("returnvalues", [])):
            _prepare_lua_parameter(parameter, current_page, targets)
        if element_type in ("CONSTANT", "VARIABLE"):
            element["is_enum_member"] = False
            element["value_type"] = _joined_parameter_type(
                element.get("parameters", []),
                "integer" if element_type == "CONSTANT" else "any")
        elif element_type == "TYPEDEF":
            element["target_type"] = _joined_parameter_type(
                element.get("parameters", []), "any")
            element["target_type_html"] = link_lua_type(
                element["target_type"], current_page, targets)
        elif element_type in ("STRUCT", "CLASS"):
            for member in element.get("members", []):
                name = member.get("name", "")
                member["is_optional"] = name.endswith("?")
                member["display_name"] = name[:-1] if name.endswith("?") else name
                member["type_html"] = link_lua_type(
                    member.get("type", ""), current_page, targets)
                member["doc"] = _link_lua_type_spans(
                    member.get("doc", ""), current_page, targets)

    for enum in (
            element for element in api.get("elements", [])
            if element.get("type") == "ENUM"):
        enum_name = enum["name"]
        enum["value_type"] = _joined_parameter_type(
            enum.get("parameters", []), "integer")
        enum["value_type_html"] = link_lua_type(
            enum["value_type"], current_page, targets)
        documented_members = {
            _qualified_enum_member_name(enum_name, member.get("name", "")): member
            for member in enum.get("members", [])
            if member.get("name")
        }
        member_names = list(documented_members)
        if not member_names:
            raise ValueError(
                "enum %s must declare at least one explicit member"
                % enum_name)

        resolved_members = []
        for member_name in member_names:
            constant = constants.get(member_name)
            if constant:
                raise ValueError(
                    "enum %s member %s is also declared as a standalone "
                    "constant" % (enum_name, member_name))
            documented = documented_members.get(member_name, {})
            resolved_members.append({
                "name": member_name,
                "doc": _link_lua_type_spans((
                    documented.get("doc")
                    or ""), current_page, targets),
            })
        enum["members"] = resolved_members

    return api
