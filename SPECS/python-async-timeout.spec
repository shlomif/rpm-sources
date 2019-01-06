# Created by pyp2rpm-3.3.2
%global pypi_name async-timeout

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        %mkrel 1
Summary:        Timeout context manager for asyncio programs
Group:          Development/Python
License:        Apache 2
URL:            https://github.com/aio-libs/async_timeout/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
async-timeout asyncio-compatible timeout context manager. Usage example - The
context manager is useful in cases when you want to apply timeout

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
async-timeout asyncio-compatible timeout context manager. Usage example - The
context manager is useful in cases when you want to apply timeout


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
%{python3_sitelib}/async_timeout
%{python3_sitelib}/async_timeout-%{version}-py?.?.egg-info
