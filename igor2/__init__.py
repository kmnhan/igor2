# flake8: noqa: F401
"""Interface for reading binary IGOR files."""
try:
    from ._version import __version__, __version_tuple__
except ImportError:
    # semver not working on Python 3.6
    __version__ = "unknown"


from . import binarywave
