# Created by pyp2rpm-3.3.2
%global pypi_name autobahn

Name:           python-%{pypi_name}
Version:        18.12.1
Release:        %mkrel 1
Summary:        WebSocket client & server library, WAMP real-time framework
Group:          Development/Python
License:        MIT License
URL:            http://crossbar.io/autobahn
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(argon2-cffi) >= 18.1.0
BuildRequires:  python3dist(awscli)
BuildRequires:  python3dist(cbor) >= 1.0.0
BuildRequires:  python3dist(cffi) >= 1.11.5
BuildRequires:  python3dist(flake8) >= 2.5.1
BuildRequires:  python3dist(lz4) >= 0.7.0
BuildRequires:  python3dist(mock) >= 1.3.0
BuildRequires:  python3dist(passlib)
BuildRequires:  python3dist(passlib) >= 1.7.1
BuildRequires:  python3dist(pep8-naming) >= 0.3.3
BuildRequires:  python3dist(py-ubjson) >= 0.8.4
BuildRequires:  python3dist(pyenchant) >= 1.6.6
BuildRequires:  python3dist(pyflakes) >= 1.0.0
BuildRequires:  python3dist(pynacl) >= 1.0.1
BuildRequires:  python3dist(pyopenssl) >= 16.2.0
BuildRequires:  python3dist(pyqrcode) >= 1.1
BuildRequires:  python3dist(pytest) < 3.3.0
BuildRequires:  python3dist(pytest) >= 2.8.6
BuildRequires:  python3dist(pytest-aiohttp)
BuildRequires:  python3dist(pytest-asyncio) < 0.6
BuildRequires:  python3dist(python-snappy) >= 0.5
BuildRequires:  python3dist(pytrie) >= 0.2
BuildRequires:  python3dist(qualname)
BuildRequires:  python3dist(service-identity) >= 16.0.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.11.0
BuildRequires:  python3dist(sphinx) >= 1.2.3
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.9
BuildRequires:  python3dist(sphinxcontrib-spelling) >= 2.1.2
BuildRequires:  python3dist(twine) >= 1.6.5
BuildRequires:  python3dist(twisted) >= 12.1.0
BuildRequires:  python3dist(txaio) >= 18.8.1
BuildRequires:  python3dist(u-msgpack-python) >= 2.1
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(wsaccel) >= 0.6.2
BuildRequires:  python3dist(zope.interface) >= 3.6.0

%description
Autobahn\|Python WebSocket & WAMP for Python on Twisted and asyncio.| |Version|
|Build Status| |Coverage| |Docs| |Docker|--| **Quick Links**: Source Code < -
Documentation < - WebSocket Examples < - WAMP Examples < | **Community**:
Mailing list < - StackOverflow < - Twitter < - IRC autobahn/chat.freenode.net <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(argon2-cffi) >= 18.1.0
Requires:       python3dist(cbor) >= 1.0.0
Requires:       python3dist(cffi) >= 1.11.5
Requires:       python3dist(lz4) >= 0.7.0
Requires:       python3dist(passlib) >= 1.7.1
Requires:       python3dist(py-ubjson) >= 0.8.4
Requires:       python3dist(pynacl) >= 1.0.1
Requires:       python3dist(pyopenssl) >= 16.2.0
Requires:       python3dist(pyqrcode) >= 1.1
Requires:       python3dist(python-snappy) >= 0.5
Requires:       python3dist(pytrie) >= 0.2
Requires:       python3dist(service-identity) >= 16.0.0
Requires:       python3dist(six) >= 1.11.0
Requires:       python3dist(twisted) >= 12.1.0
Requires:       python3dist(txaio) >= 18.8.1
Requires:       python3dist(u-msgpack-python) >= 2.1
Requires:       python3dist(wsaccel) >= 0.6.2
Requires:       python3dist(zope.interface) >= 3.6.0
%description -n python3-%{pypi_name}
Autobahn\|Python WebSocket & WAMP for Python on Twisted and asyncio.| |Version|
|Build Status| |Coverage| |Docs| |Docker|--| **Quick Links**: Source Code < -
Documentation < - WebSocket Examples < - WAMP Examples < | **Community**:
Mailing list < - StackOverflow < - Twitter < - IRC autobahn/chat.freenode.net <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/twisted
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
