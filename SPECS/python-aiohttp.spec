# Created by pyp2rpm-3.3.2
%global pypi_name aiohttp

Name:           python-%{pypi_name}
Version:        3.5.1
Release:        %mkrel 1
Summary:        Async http client/server framework (asyncio)
Group:          Development/Python
License:        Apache 2
URL:            https://github.com/aio-libs/aiohttp
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(aiodns)
BuildRequires:  python3dist(async-generator)
BuildRequires:  python3dist(async-timeout) < 4.0
BuildRequires:  python3dist(async-timeout) >= 3.0
BuildRequires:  python3dist(attrs) >= 17.3.0
BuildRequires:  python3dist(brotlipy)
BuildRequires:  python3dist(cchardet)
BuildRequires:  python3dist(chardet) < 4.0
BuildRequires:  python3dist(chardet) >= 2.0
BuildRequires:  python3dist(gunicorn)
BuildRequires:  python3dist(idna-ssl) >= 1.0
BuildRequires:  python3dist(multidict) < 5.0
BuildRequires:  python3dist(multidict) >= 4.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-timeout)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(typing-extensions) >= 3.6.5
BuildRequires:  python3dist(yarl) < 2.0
BuildRequires:  python3dist(yarl) >= 1.0
BuildRequires:  python3dist(sphinx)

%description
 Async http client/server framework :height: 64px :width: 64px| :alt: AppVeyor
status for master branch

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(aiodns)
Requires:       python3dist(async-timeout) < 4.0
Requires:       python3dist(async-timeout) >= 3.0
Requires:       python3dist(attrs) >= 17.3.0
Requires:       python3dist(brotlipy)
Requires:       python3dist(cchardet)
Requires:       python3dist(chardet) < 4.0
Requires:       python3dist(chardet) >= 2.0
Requires:       python3dist(idna-ssl) >= 1.0
Requires:       python3dist(multidict) < 5.0
Requires:       python3dist(multidict) >= 4.0
Requires:       python3dist(typing-extensions) >= 3.6.5
Requires:       python3dist(yarl) < 2.0
Requires:       python3dist(yarl) >= 1.0
%description -n python3-%{pypi_name}
 Async http client/server framework :height: 64px :width: 64px| :alt: AppVeyor
status for master branch

%package -n python-%{pypi_name}-doc
Summary:        aiohttp documentation
%description -n python-%{pypi_name}-doc
Documentation for aiohttp

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
%license LICENSE.txt vendor/http-parser/LICENSE-MIT
%doc README.rst vendor/http-parser/README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt vendor/http-parser/LICENSE-MIT
