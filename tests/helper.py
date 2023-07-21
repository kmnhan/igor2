import pathlib
from pprint import pformat

from igor2.binarywave import load as loadibw

data_dir = pathlib.Path(__file__).parent / "data"


def assert_equal_dump_no_whitespace_no_byte(data_a, data_b):
    def repl(x):
        return x.replace(
            " ", "").replace(
            "b'", "'").replace(
            "\n", "").replace(
            "float32", "'>f4'")

    assert repl(data_a) == repl(data_b)


def dumpibw(filename):
    path = data_dir / filename
    data = loadibw(path)
    return format_data(data)


def format_data(data):
    lines = pformat(data).splitlines()
    return '\n'.join([line.rstrip() for line in lines])


def walk_callback(dirpath, key, value):
    return 'walk callback on ({}, {}, {})'.format(
        dirpath, key, '{...}' if isinstance(value, dict) else value)
