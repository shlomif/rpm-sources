# Created by pyp2rpm-3.3.2
%global pypi_name async-generator

Name:           python-%{pypi_name}
Version:        1.10
Release:        %mkrel 1
Summary:        Async generators and context managers for Python 3
Group:          Development/Python
License:        MIT -or- Apache License 2.0
URL:            https://github.com/python-trio/async_generator
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/async_generator-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
 :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 :target:

%package -n python-%{pypi_name}-doc
Summary:        async-generator documentation
%description -n python-%{pypi_name}-doc
Documentation for async-generator

%prep
%autosetup -n async_generator-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
# PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.MIT LICENSE LICENSE.APACHE2
%doc README.rst
%{python3_sitelib}/async_generator
%{python3_sitelib}/async_generator-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
#doc html
%license LICENSE.MIT LICENSE LICENSE.APACHE2
