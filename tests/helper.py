import pathlib
from pprint import pformat

from igor2.binarywave import load as loadibw

data_dir = pathlib.Path(__file__).parent / "data"


def assert_equal_dump_no_whitespace_no_byte(data_a, data_b):
    def repl(x):
        for old, new in [
            [" ", ""],  # ignore whitespaces
            ["b'", "'"],  # ignore bytes vs str
            ["\n", ""],  # ignore newlines
            # teat all floats as equal
            ["float32", "float"],
            ["float64", "float"],
            ["'>f4'", "float"],
            ["'>f8'", "float"],
        ]:
            x = x.replace(old, new)
        return x

    a = repl(data_a)
    b = repl(data_b)
    print("DBUG data_a: ", a)
    print("DBUG data_b: ", b)
    assert a == b


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
