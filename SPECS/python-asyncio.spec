# Created by pyp2rpm-3.3.2
%global pypi_name asyncio

Name:           python-%{pypi_name}
Version:        3.4.3
Release:        %mkrel 1
Summary:        reference implementation of PEP 3156
Group:          Development/Python
License:        None
URL:            http://www.python.org/dev/peps/pep-3156/
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Tulip is the codename for my reference implementation of PEP 3156.PEP 3156:
This requires Python 3.3 or later! ***Copyright/license: Open source, Apache
2.0. Enjoy.Master Mercurial repo: actual code lives in the 'asyncio'
subdirectory. Tests are in the 'tests' subdirectory.To run tests: - make testTo
run coverage (coverage package is required): - make coverageOn Windows, things
are a little...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Tulip is the codename for my reference implementation of PEP 3156.PEP 3156:
This requires Python 3.3 or later! ***Copyright/license: Open source, Apache
2.0. Enjoy.Master Mercurial repo: actual code lives in the 'asyncio'
subdirectory. Tests are in the 'tests' subdirectory.To run tests: - make testTo
run coverage (coverage package is required): - make coverageOn Windows, things
are a little...


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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
