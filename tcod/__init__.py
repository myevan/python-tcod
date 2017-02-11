"""
    This module provides a simple CFFI API to libtcod.

    This port has large partial support for libtcod's C functions.
    Use tcod/libtcod_cdef.h in the source distribution to see specially what
    functions were exported and what new functions have been added by TDL.

    The ffi and lib variables should be familiar to anyone that has used CFFI
    before, otherwise it's time to read up on how they work:
    https://cffi.readthedocs.org/en/latest/using.html

    Otherwise this module can be used as a drop in replacement for the official
    libtcod.py module.

    Bring any issues or requests to GitHub:
    https://github.com/HexDecimal/libtcod-cffi
"""
from __future__ import absolute_import as _

from tcod.libtcodpy import *
from tcod.tcod import *
from tcod import path
from tcod.version import __version__
