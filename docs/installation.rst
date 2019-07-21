Installation 설치
============
Once installed, you'll be able to import the `tcod` and `libtcodpy` modules,
as well as the deprecated `tdl` module.
설치가 완료되면 `tcod` 와 `libtcopy` 모듈 그리고 디프리케이티드된 `tdl`모듈을 임포트할 수 있습니다.

Python 3.5 or above is required for a normal install.
These instructions include installing Python if you don't have it yet.
일반 설치에서는 파이썬 3.5 이상을 필요로 합니다. 현재 문서에서는 파이썬이 설치되어 있지 않은 경우를 위해 파이썬 설치 방법도 포함되어있습니다.

There are known issues in very old versions of pip.
If pip fails to install python-tcod then try updating it first.
아주 오래된 pip 버전을 사용할 경우 이슈가 발생할 수 있습니다. pip 로 python-tcod 설치에 실패할 경우 업그레이드를 추천합니다.

Windows 윈도우
-------
`First install a recent version of Python 3.
<https://www.python.org/downloads/>`_
Make sure Python is added to the Windows `PATH`.
`Python 3 최신 버전을 먼저 설치해주세요. <https://www.python.org/downloads/>`_
윈도우 환경 변수 `PATH` 에 파이썬을 반드시 추가해야 합니다.

If you don't already have it, then install the latest
`Microsoft Visual C++ Redistributable
<https://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads>`_.
**vc_redist.x86.exe** for a 32-bit install of Python, or **vc_redist.x64.exe**
for a 64-bit install.  You'll need to keep this in mind when distributing any
libtcod program to end-users.
`Microsoft Visual C++ Redistributable
<https://support.microsoft.com/en-ca/help/2977003/the-latest-supported-visual-c-downloads>`_ 을 아직 설치하지 않았다면 최신 버전으로 설치하시기 바랍니다.
32비트 파이썬을 사용중이라면 **vc_redist.x86.exe**, 64비트라면 **vc_redist.x64.exe** 을 설치해야 합니다.
libtcod 프로그램을 최종 사용자에게 배포할때도 이점을 기억해두셔야 합니다.

Then to install python-tcod run the following from a Windows command line::
윈도우 커맨드 라인에서 아래 문구를 실행해 python-tcod 를 설치할 수 있습니다::

    py -m pip install tcod

If Python was installed for all users then you may need to add the ``--user``
flag to pip.
만약 모든 유저용으로 파이썬이 설치되었다면 pip 실행시 ``--user`` 플래그를 추가해주세요.

MacOS 맥 OS
-----
The latest version of python-tcod only supports MacOS 10.9 (Mavericks) or
later.
python-tcod 최신 버전은 맥 OS 10.9 (매버릭스) 이상만 지원합니다.

`First install a recent version of Python 3.
<https://www.python.org/downloads/>`_
`Python 3 최신 버전을 먼저 설치해주세요. <https://www.python.org/downloads/>`_

Then to install using pip in a user environment, use the following command::
유저 환경에서 pip 를 사용해 설치한다면 아래 명령을 사용해주시기 바랍니다::

    python3 -m pip install --user tcod

Linux (Debian-based) 리눅스 (데비안 계열)
--------------------
On Linux python-tcod will need to be built from source.
You can run this command to download python-tcod's dependencies with apt::
리눅스에서 python-tcod 를 사용하려면 소스 빌드가 필요합니다. 아래 명령을 사용하면 apt 를 통해 python-tcod 의 디펜던시를 다운로드 받으실 수 있습니다.

    sudo apt install build-essential python3-dev python3-pip python3-numpy libsdl2-dev libffi-dev libomp5

If your GCC version is less than 6.1, or your SDL version is less than 2.0.5,
then you will need to perform a distribution upgrade before continuing.
GCC 버전이 6.1 보다 낮거나 SDL 버전이 2.0.5 이하라면 설치를 계속하기전에 배포판 업그레이드를 할 필요가 있습니다.

Once dependences are resolved you can build and install python-tcod using pip
in a user environment::
디펜던시 이슈가 해소되면 pip 를 통해 유저 환경에 python-tcod 를 빌드하고 설치하실 수 있습니다.

    python3 -m pip install --user tcod

Upgrading python-tcod 업그레이드
---------------------
python-tcod is updated often, you can re-run pip with the ``--upgrade`` flag
to ensure you have the latest version, for example::
python-tcod 는 자주 업데이트되기 때문에, pip 에 ``--upgrade`` 를 붙여 최신 버전으로 재설치할 필요가 있습니다. 예를 들면 다음과 같습니다::

    python3 -m pip install --upgrade tcod

Upgrading from libtcodpy to python-tcod libtcodpy 에서 python-tcod 로 이전
---------------------------------------
`libtcodpy` is no longer maintained and using it can make it difficult to
collaborate with developers across multiple operating systems, or to distribute
to those platforms.
New API features are only available on `python-tcod`.
`libtcodpy` 는 더 이상 유지보수되지 않으며 다양한 OS 하에 있는 개발자들과 협업하거나 배포하기 어렵습니다.

You can recognise a libtcodpy program because it includes this file structure::
libtcodpy 프로그램에는 아래와 같은 파일 구조가 존재하므로 구분이 가능합니다.

    libtcodpy/
    libtcod.dll
    SDL2.dll

First make sure your libtcodpy project works in Python 3.  libtcodpy
already supports both 2 and 3 so you don't need to worry about updating it,
but you will need to worry about bit-size.  If you're using a
32-bit version of Python 2 then you'll need to upgrade to a 32-bit version of
Python 3 until libtcodpy can be completely removed.
먼저 libtcodpy 프로젝트가 파이썬3 에서 작동하는지 확인 해보시기 바랍니다. 
libtcodpy 는 파이썬2 와 파이썬3 을 모두 지원하므로 업데이트하는 것에 대해 걱정할 필요는 없지만 비트에 대해서는 신경을 쓰셔야 합니다.
32 비트 파이썬2 버전을 사용중이라면 libtcodpy 를 완전히 제거한 다음 32 비트 파이썬3 버전으로 업그레이드하시기 바랍니다.

Once you've installed python-tcod you can safely delete the ``libtcodpy/``
folder and all DLL files of a libtcodpy program, python-tcod will
seamlessly take the place of libtcodpy's API.
일단 python-tcod 를 설치했다면 libtcodpy/ 폴더와 libtcodpy 프로그램의 모든 DLL 파일을 삭제하셔도 무방합니다.
python-tcod 가 libtcodpy의 API를 대신하게 됩니다.

From then on anyone can follow the instructions to install python-tcod and your
project will work for them regardless of their platform or bit-size.
이후 python-tcod 설치 방법을 따라하시면 됩니다. 프로젝트는 플랫폼이나 비트 크기에 상관없이 작동하게 될 것입니다.

Distributing 배포
------------
Once your project is finished, it can be distributed using
`PyInstaller <https://www.pyinstaller.org/>`_.
프로젝트 작업이 완료되면 `PyInstaller <https://www.pyinstaller.org/>`_. 을 사용해 배포하실 수 있습니다.

Python 2.7 파이썬 2.7
----------
While it's not recommended, you can still install `python-tcod` on
`Python 2.7`.
추천하지는 않지만 아직 `Python 2.7` 에 `python-tcod` 를 설치할 수 있습니다.

`Keep in mind the Python 2's end-of-life is the year 2020.  You should not be
starting any new projects in Python 2!
<https://pythonclock.org/>`_
파이썬2 의 수명은 2020 년까지라는 것을 명심해두시기 바랍니다. 새로운 프로젝트를 파이썬2 로 시작하지 마세요! <https://pythonclock.org/>`_

Follow the instructions for your platform normally.  When it comes to
install with pip, tell it to get python-tcod version 6::
플랫폼에 맞는 설치 방법을 따르시기 바랍니다. pip 설치라면 python-tcod 6 버전을 사용하면 됩니다.

    python2 -m pip install tcod==6.0.7
