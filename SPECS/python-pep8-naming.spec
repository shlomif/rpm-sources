# Created by pyp2rpm-3.3.2
%global pypi_name pep8-naming

Name:           python-%{pypi_name}
Version:        0.7.0
Release:        %mkrel 1
Summary:        Check PEP-8 naming conventions, plugin for flake8
Group:          Development/Python
License:        Expat license
URL:            https://github.com/PyCQA/pep8-naming
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
PEP-8 Naming Conventions Check the PEP-8 naming conventions.This module
provides a plugin for flake8, the Python code checker.(It replaces the plugin
flint- naming for the flint checker.) Installation You can install, upgrade,
uninstall pep8-naming with these commands:: $ pip install pep8-naming $ pip
install --upgrade pep8-naming $ pip uninstall pep8-naming Plugin for Flake8
--When both...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flake8-polyfill) < 2
Requires:       python3dist(flake8-polyfill) >= 1.0.2
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
PEP-8 Naming Conventions Check the PEP-8 naming conventions.This module
provides a plugin for flake8, the Python code checker.(It replaces the plugin
flint- naming for the flint checker.) Installation You can install, upgrade,
uninstall pep8-naming with these commands:: $ pip install pep8-naming $ pip
install --upgrade pep8-naming $ pip uninstall pep8-naming Plugin for Flake8
--When both...


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
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pep8ext_naming.py
%{python3_sitelib}/pep8_naming-%{version}-py?.?.egg-info
