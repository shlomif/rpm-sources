# Created by pyp2rpm-3.3.2
%global pypi_name idna-ssl

Name:           python-%{pypi_name}
Version:        1.1.0
Release:        %mkrel 1
Summary:        Patch ssl.match_hostname for Unicode(idna) domains support
Group:          Development/Python
License:        None
URL:            https://github.com/aio-libs/idna-ssl
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(idna) >= 2.0
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)

%description
:info: Patch ssl.match_hostname for Unicode(idna) domains support Installation
.. code-block:: shell pip install idna-sslUsage .. code-block:: python from
idna_ssl import patch_match_hostname noqa isort:skip patch_match_hostname()
noqa isort:skip

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(idna) >= 2.0
%description -n python3-%{pypi_name}
:info: Patch ssl.match_hostname for Unicode(idna) domains support Installation
.. code-block:: shell pip install idna-sslUsage .. code-block:: python from
idna_ssl import patch_match_hostname noqa isort:skip patch_match_hostname()
noqa isort:skip


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
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/idna_ssl.py
%{python3_sitelib}/idna_ssl-%{version}-py?.?.egg-info
