#!/usr/bin/env python

from collections.abc import Mapping, Iterable
from numbers import Number

from os.path import normpath


def format_realpath(value):
    # note! realpath will follow symlinks, e.g. /var => /private/var on OSX
    return normpath(value).replace("//", "/")


def format_toml_simple(value):
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
    return "\n".join("{} = {}".format(k, format_toml_simple(v)) for k, v in value.items())


def format_toml_symbols(symbols):
    def _helper(value):
        return value if isinstance(value, Mapping) else dict(include=value)

    if isinstance(symbols, Mapping):
        return "\n[symbols]\n{}".format(_format_toml_mapping(_helper(symbols)))

    def _helper_fix_bridge_1(value):
        return "regex={}\n".format(format_toml_simple(value))

    def _helper_fix_bridge_2(key, value):
        return "[symbols.{}]\n{}\n".format(key, _helper_fix_bridge_1(value))

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
        return "\n[symbols]\n{}".format(_helper_fix_bridge(symbols))

    return "\nsymbols = {}".format(format_toml_simple(symbols))


def format_toml_accounts(accounts):
    def _helper(key, value):
        return "\n[accounts.{}]\n{}".format(key, _format_toml_mapping(value))

    return "\n[accounts]\n{}".format("\n".join(_helper(k, v) for k, v in accounts.items()))


def format_toml_users(users):
    def _helper(key, value):
        return "\n[users.{}]\n{}".format(key, _format_toml_mapping(value))

    return "\n[users]\n{}".format("\n".join(_helper(k, v) for k, v in users.items()))


def format_toml_statistics(statistics):
    def _helper(key, value):
        return "\n[statistics.{}]\n{}".format(key, _format_toml_mapping(value))

    return "\n[statistics]\n{}".format("\n".join(_helper(k, v) for k, v in statistics.items()))


def format_gflags_options(options):
    def _helper(key, value):
        return "--{}={}".format(key, value)

    return "\n".join(_helper(k, v) for k, v in options.items())


class FilterModule(object):
    def filters(self):
        return dict(
            roq_realpath=format_realpath,
            roq_toml_simple=format_toml_simple,
            roq_toml_symbols=format_toml_symbols,
            roq_toml_accounts=format_toml_accounts,
            roq_toml_users=format_toml_users,
            roq_toml_statistics=format_toml_statistics,
            roq_gflags_options=format_gflags_options,
        )
