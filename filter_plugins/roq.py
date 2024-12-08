#!/usr/bin/env python

import json
import toml

from collections.abc import Mapping, Iterable
from numbers import Number


def _format_toml_simple(value):
    if isinstance(value, Mapping):
        assert False, "mapping not allowed"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, Number):
        return "{}".format(value)
    elif isinstance(value, str):
        return '"{}"'.format(value)
    elif isinstance(value, Iterable):
        return '["{}"]'.format('", "'.join(value))
    else:
        assert False, "unknown type"


def _format_toml_mapping(value):
    assert isinstance(value, Mapping), "not a mapping"
    return "\n".join("{} = {}".format(k, _format_toml_simple(v)) for k, v in value.items())


def format_toml_symbols(symbols):
    def _helper(value):
        return value if isinstance(value, Mapping) else dict(include=value)

    if isinstance(symbols, Mapping):
        return "\n[symbols]\n{}".format(_format_toml_mapping(_helper(symbols)))

    def _helper_fix_bridge_1(value):
        return "regex={}".format(_format_toml_simple(value))

    def _helper_fix_bridge_2(key, value):
        return "\n\n[symbols.{}]\n{}".format(key, _helper_fix_bridge_1(value))

    def _helper_fix_bridge(value):
        result = ""
        for item in value:
            if isinstance(item, Mapping):
                for key_2, value_2 in item.items():
                    result = result + _helper_fix_bridge_2(key_2, value_2)
            else:
                result = result + _helper_fix_bridge_1(item)
        return result

    if isinstance(symbols, list):
        is_fix_bridge = False
        for item in symbols:
            is_fix_bridge = is_fix_bridge or isinstance(item, Mapping)
        if is_fix_bridge:
            return "\n[symbols]\n{}".format(_helper_fix_bridge(symbols))

    return "\nsymbols = {}".format(_format_toml_simple(symbols))


def format_gflags_options(options):
    def _helper(key, value):
        return "--{}={}".format(key, value)

    if options is None or len(options) == 0:
        return ""

    return "\n{}".format("\n".join(_helper(k, v) for k, v in options.items()))


def format_toml(value):
    tmp_1 = json.dumps(dict(value))
    tmp_2 = json.loads(tmp_1)
    return toml.dumps(tmp_2)


class FilterModule(object):
    def filters(self):
        return dict(
            roq_toml_symbols=format_toml_symbols,
            roq_gflags_options=format_gflags_options,
            roq_toml=format_toml,
        )
