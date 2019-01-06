# Created by pyp2rpm-3.3.2
%global pypi_name pycares

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        %mkrel 1
Summary:        Python interface for c-ares
Group:          Development/Python
License:        None
URL:            http://github.com/saghul/pycares
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
 pycares: Python interface for c-ares pycares is a Python module which provides
an interface to c-ares. c-ares <>_ is a C library that performs DNS requests
and name resolutions asynchronously.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 pycares: Python interface for c-ares pycares is a Python module which provides
an interface to c-ares. c-ares <>_ is a C library that performs DNS requests
and name resolutions asynchronously.

%package -n python-%{pypi_name}-doc
Summary:        pycares documentation
%description -n python-%{pypi_name}-doc
Documentation for pycares

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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
