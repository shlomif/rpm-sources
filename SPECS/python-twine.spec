# Created by pyp2rpm-3.3.2
%global pypi_name twine

Name:           python-%{pypi_name}
Version:        1.13.0
Release:        %mkrel 1
Summary:        Collection of utilities for publishing packages on PyPI
Group:          Development/Python
License:        Apache License, Version 2.0
URL:            https://twine.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildConflicts: python3dist(requests) = 2.15
BuildConflicts: python3dist(requests) = 2.16
BuildConflicts: python3dist(requests-toolbelt) = 0.9.0
BuildRequires:  python3dist(keyring)
BuildRequires:  python3dist(pkginfo) >= 1.4.2
BuildRequires:  python3dist(pyblake2)
BuildRequires:  python3dist(readme-renderer) >= 21.0
BuildRequires:  python3dist(requests) >= 2.5.0
BuildRequires:  python3dist(requests-toolbelt) >= 0.8.0
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 0.7.0
BuildRequires:  python3dist(tqdm) >= 4.14
BuildRequires:  python3dist(sphinx)

%description
twine .. rtd-inclusion-marker-do-not-removeTwine is a utility_ for publishing_
Python packages on PyPI_.It provides build system independent uploads of source
and binary distribution artifacts <distributions>_ for both new and existing
projects_. Why Should I Use This? -The goal of twine is to improve PyPI
interaction by improving security and testability.The biggest reason to use
twine is...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Conflicts:      python3dist(requests) = 2.15
Conflicts:      python3dist(requests) = 2.16
Conflicts:      python3dist(requests-toolbelt) = 0.9.0
Requires:       python3dist(keyring)
Requires:       python3dist(pkginfo) >= 1.4.2
Requires:       python3dist(pyblake2)
Requires:       python3dist(readme-renderer) >= 21.0
Requires:       python3dist(requests) >= 2.5.0
Requires:       python3dist(requests-toolbelt) >= 0.8.0
Requires:       python3dist(setuptools)
Requires:       python3dist(setuptools) >= 0.7.0
Requires:       python3dist(tqdm) >= 4.14
%description -n python3-%{pypi_name}
twine .. rtd-inclusion-marker-do-not-removeTwine is a utility_ for publishing_
Python packages on PyPI_.It provides build system independent uploads of source
and binary distribution artifacts <distributions>_ for both new and existing
projects_. Why Should I Use This? -The goal of twine is to improve PyPI
interaction by improving security and testability.The biggest reason to use
twine is...

%package -n python-%{pypi_name}-doc
Summary:        twine documentation
%description -n python-%{pypi_name}-doc
Documentation for twine

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
%{_bindir}/twine
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
