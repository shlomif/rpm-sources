# Created by pyp2rpm-3.3.2
%global pypi_name sphinx-bootstrap-theme

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        %mkrel 1
Summary:        Sphinx Bootstrap Theme
Group:          Development/Python
License:        None
URL:            http://ryan-roemer.github.com/sphinx-bootstrap-theme/README.html
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Sphinx Bootstrap Theme This Sphinx_ theme_ integrates the Bootstrap_ CSS /
JavaScript framework with various layout options, hierarchical menu navigation,
and mobile-friendly responsive design. It is configurable, extensible, and can
use any number of different Bootswatch_ CSS themes... _Bootstrap: .. _Sphinx:
.. _theme: .. _PyPI: .. _GitHub repository: Introduction and Demos

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 Sphinx Bootstrap Theme This Sphinx_ theme_ integrates the Bootstrap_ CSS /
JavaScript framework with various layout options, hierarchical menu navigation,
and mobile-friendly responsive design. It is configurable, extensible, and can
use any number of different Bootswatch_ CSS themes... _Bootstrap: .. _Sphinx:
.. _theme: .. _PyPI: .. _GitHub repository: Introduction and Demos


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.txt README.rst
%{python3_sitelib}/sphinx_bootstrap_theme
%{python3_sitelib}/sphinx_bootstrap_theme-%{version}-py?.?.egg-info
