# Created by pyp2rpm-3.3.2
%global pypi_name txaio

Name:           python-%{pypi_name}
Version:        18.8.1
Release:        %mkrel 1
Summary:        Compatibility API between asyncio/Twisted/Trollius
Group:          Development/Python
License:        MIT License
URL:            https://github.com/crossbario/txaio
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pep8) >= 1.6.2
BuildRequires:  python3dist(pyenchant) >= 1.6.6
BuildRequires:  python3dist(pytest) >= 2.6.4
BuildRequires:  python3dist(pytest-cov) >= 1.8.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx) >= 1.2.3
BuildRequires:  python3dist(sphinx-rtd-theme) >= 0.1.9
BuildRequires:  python3dist(sphinxcontrib-spelling) >= 2.1.2
BuildRequires:  python3dist(tox) >= 2.1.1
BuildRequires:  python3dist(twine) >= 1.6.5
BuildRequires:  python3dist(twisted) >= 12.1.0
BuildRequires:  python3dist(twisted) >= 12.1.0
BuildRequires:  python3dist(wheel)
BuildRequires:  python3dist(zope.interface) >= 3.6
BuildRequires:  python3dist(zope.interface) >= 3.6
BuildRequires:  python3dist(sphinx)

%description
| |Version| |Build Status| |Coverage| |Docs|--**txaio** is a helper library for
writing code that runs unmodified on both Twisted < and asyncio < / Trollius <
is like six < but for wrapping over differences between Twisted and asyncio so
one can write code that runs unmodified on both (aka *source code
compatibility*). In other words: your *users* can choose if they want asyncio
**or** Twisted...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(six)
Requires:       python3dist(twisted) >= 12.1.0
Requires:       python3dist(twisted) >= 12.1.0
Requires:       python3dist(zope.interface) >= 3.6
Requires:       python3dist(zope.interface) >= 3.6
%description -n python3-%{pypi_name}
| |Version| |Build Status| |Coverage| |Docs|--**txaio** is a helper library for
writing code that runs unmodified on both Twisted < and asyncio < / Trollius <
is like six < but for wrapping over differences between Twisted and asyncio so
one can write code that runs unmodified on both (aka *source code
compatibility*). In other words: your *users* can choose if they want asyncio
**or** Twisted...

%package -n python-%{pypi_name}-doc
Summary:        txaio documentation
%description -n python-%{pypi_name}-doc
Documentation for txaio

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
