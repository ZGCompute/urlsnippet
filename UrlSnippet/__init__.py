from .version import __version__
from .server import UrlSnippet

# if somebody does "from UrlSnippet import *", this is what they will
# be able to access:
__all__ = [
    'server'
]
