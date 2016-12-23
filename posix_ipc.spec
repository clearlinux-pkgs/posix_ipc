#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : posix_ipc
Version  : 1.0.0
Release  : 22
URL      : https://pypi.python.org/packages/source/p/posix_ipc/posix_ipc-1.0.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/posix_ipc/posix_ipc-1.0.0.tar.gz
Summary  : POSIX IPC primitives (semaphores, shared memory and message queues) for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: posix_ipc-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
posix_ipc is a Python module (written in C) that permits creation and
manipulation of POSIX inter-process semaphores, shared memory and message
queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX
1003.1b-1993. This includes nearly all Unices and Windows + Cygwin 1.7.

%package python
Summary: python components for the posix_ipc package.
Group: Default

%description python
python components for the posix_ipc package.


%prep
%setup -q -n posix_ipc-1.0.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
