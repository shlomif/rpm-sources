# Created by pyp2rpm-3.3.2
%global pypi_name pytest-asyncio

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        %mkrel 1
Summary:        Pytest support for asyncio
Group:          Development/Python
License:        Apache 2.0
URL:            https://github.com/pytest-dev/pytest-asyncio
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pytest-asyncio: pytest support for asyncio :alt: Supported Python versions

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(async-generator) >= 1.3
Requires:       python3dist(async-generator) >= 1.3
Requires:       python3dist(coverage)
Requires:       python3dist(hypothesis) >= 3.64
Requires:       python3dist(pytest) >= 3.0.6
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
pytest-asyncio: pytest support for asyncio :alt: Supported Python versions


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_asyncio
%{python3_sitelib}/pytest_asyncio-%{version}-py?.?.egg-info
