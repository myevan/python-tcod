.. contents::
   :backlinks: top

========
 Status 상태
========
|VersionsBadge| |ImplementationBadge| |LicenseBadge|

|PyPI| |RTD| |Appveyor| |Travis| |Coveralls| |Codecov| |Codacy|

|Requires| |Pyup|

=======
 About 정보
=======
This is a Python cffi_ port of libtcod_.
python-tcod 는 libtcod_ 의 파이썬 cffi_ 포팅이며

This library is `hosted on GitHub <https://github.com/libtcod/python-tcod>`_.
`GitHub <https://github.com/libtcod/python-tcod>`_ 에서 호스팅되고 있습니다.

Any issues you have with this module can be reported at the
`GitHub issue tracker <https://github.com/libtcod/python-tcod/issues>`_.
이슈가 있을 경우 `GitHub issue tracker <https://github.com/libtcod/python-tcod/issues>`_ 로 리포트 부탁드립니다.

=======
 Usage 사용법
=======
This module was designed to be backward compatible with the original libtcodpy
module distributed with libtcod.
python-tcod 는 libtcod 에서 배포하는 libtcodpy 와 역호환되도록 설계되었습니다.

If you had code that runs on libtcodpy then you can use this library as a
drop-in replacement.  This installs a libtcodpy module so you'll only need to
delete the libtcodpy/ folder that's usually bundled in an older libtcodpy
project. 
libtcodpy 에서 실행되는 코드는 python-tcod 에서도 사용할 수 있습니다. 
python-tcod 에는 libtcodpy 모듈을 포함하므로 기존 libtcodpy 프로젝트에 번들된 libtcodpy 폴더는 삭제해야 합니다.

Guides and Tutorials for libtcodpy should work with the tcod module.
libtcodpy 용 가이드와 튜토리얼은 tcod 모듈로 작동합니다.

The latest documentation can be found here:
최신 문서는 아래 링크에서 확인하실 수 있습니다.
https://python-tcod.readthedocs.io/en/latest/

==============
 Installation 설치
==============
Detailed installation instructions are here:
자세한 설치 방법은 아래 링크에서 확인하실 수 있습니다.
https://python-tcod.readthedocs.io/en/latest/installation.html

For the most part it's just::
가장 중요한 내용은 딱 한줄입니다.

    pip3 install tcod

==============
 Requirements 요구 사항
==============
* Python 3.5+ 
* 파이썬 3.5 이상
* Windows, Linux, or MacOS X 10.9+.
* 윈도우, 리눅스, 맥 OS 10.9 이상
* On Windows, requires the Visual C++ runtime 2015 or later.
* 윈도우의 경우 Visual C++ 런타임 2015 이상 필요
* On Linux, requires libsdl2 (2.0.5+) and libomp5 to run.
* 리눅스의 경우 libsdl2 (2.0.5 이상) 및 libomp5 필요

=========
 License 라이선스
=========
python-tcod is distributed under the `Simplified 2-clause FreeBSD license
<https://github.com/HexDecimal/python-tdl/blob/master/LICENSE.txt>`_.
python-tcod 는 `Simplified 2-clause FreeBSD license
<https://github.com/HexDecimal/python-tdl/blob/master/LICENSE.txt>`_  라이선스 하에 배포됩니다.

.. _LICENSE.txt: https://github.com/libtcod/python-tcod/blob/master/LICENSE.txt

.. _python-tdl: https://github.com/libtcod/python-tcod/

.. _cffi: https://cffi.readthedocs.io/en/latest/

.. _numpy: https://docs.scipy.org/doc/numpy/user/index.html

.. _libtcod: https://github.com/libtcod/libtcod

.. _pip: https://pip.pypa.io/en/stable/installing/

.. |VersionsBadge| image:: https://img.shields.io/pypi/pyversions/tcod.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/tcod

.. |ImplementationBadge| image:: https://img.shields.io/pypi/implementation/tcod.svg?maxAge=2592000
    :target: https://pypi.python.org/pypi/tcod

.. |LicenseBadge| image:: https://img.shields.io/pypi/l/tcod.svg?maxAge=2592000
    :target: https://github.com/HexDecimal/tcod/blob/master/LICENSE.txt

.. |PyPI| image:: https://img.shields.io/pypi/v/tcod.svg?maxAge=10800
    :target: https://pypi.python.org/pypi/tcod

.. |RTD| image:: https://readthedocs.org/projects/python-tcod/badge/?version=latest
    :target: http://python-tcod.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/bb04bpankj0h1cpa/branch/master?svg=true
    :target: https://ci.appveyor.com/project/HexDecimal/python-tdl/branch/master

.. |Travis| image:: https://travis-ci.org/libtcod/python-tcod.svg?branch=master
    :target: https://travis-ci.org/libtcod/python-tcod

.. |Coveralls| image:: https://coveralls.io/repos/github/HexDecimal/python-tdl/badge.svg?branch=master
    :target: https://coveralls.io/github/HexDecimal/python-tdl?branch=master

.. |Codecov| image:: https://codecov.io/gh/libtcod/python-tcod/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/libtcod/python-tcod

.. |Issues| image:: https://img.shields.io/github/issues/libtcod/python-tcod.svg?maxAge=3600
    :target: https://github.com/libtcod/python-tcod/issues

.. |Codacy| image:: https://api.codacy.com/project/badge/Grade/b9df9aff87fb4968a0508a72aeb74a72
    :target: https://www.codacy.com/app/4b796c65-github/python-tcod?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=libtcod/python-tcod&amp;utm_campaign=Badge_Grade

.. |Requires| image:: https://requires.io/github/libtcod/python-tcod/requirements.svg?branch=master
    :target: https://requires.io/github/libtcod/python-tcod/requirements/?branch=master
    :alt: Requirements Status

.. |Pyup| image:: https://pyup.io/repos/github/libtcod/python-tcod/shield.svg
    :target: https://pyup.io/repos/github/libtcod/python-tcod/
    :alt: Updates
