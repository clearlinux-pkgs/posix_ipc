#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : posix_ipc
Version  : 1.0.0
Release  : 28
URL      : http://pypi.debian.net/posix_ipc/posix_ipc-1.0.0.tar.gz
Source0  : http://pypi.debian.net/posix_ipc/posix_ipc-1.0.0.tar.gz
Summary  : POSIX IPC primitives (semaphores, shared memory and message queues) for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: posix_ipc-legacypython
Requires: posix_ipc-python3
Requires: posix_ipc-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
manipulation of POSIX inter-process semaphores, shared memory and message 
        queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX
        1003.1b-1993. This includes nearly all Unices and Windows + Cygwin 1.7.
        
        posix_ipc is compatible with Python 2 and 3.
        
        The latest version, contact info, sample code, etc. are available on PyPI

%package legacypython
Summary: legacypython components for the posix_ipc package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the posix_ipc package.


%package python
Summary: python components for the posix_ipc package.
Group: Default
Requires: posix_ipc-legacypython
Requires: posix_ipc-python3

%description python
python components for the posix_ipc package.


%package python3
Summary: python3 components for the posix_ipc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the posix_ipc package.


%prep
%setup -q -n posix_ipc-1.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507164336
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test-2.7 --verbose || :
%install
export SOURCE_DATE_EPOCH=1507164336
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
