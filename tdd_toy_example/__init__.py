from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("tdd-toy-example")
except PackageNotFoundError:
    # package is not installed
    pass
