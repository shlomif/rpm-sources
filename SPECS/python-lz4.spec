# Created by pyp2rpm-3.3.2
%global pypi_name lz4

Name:           python-%{pypi_name}
Version:        2.1.10
Release:        %mkrel 1
Summary:        LZ4 Bindings for Python
Group:          Development/Python
License:        None
URL:            https://github.com/python-lz4/python-lz4
Source0:        https://files.pythonhosted.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildConflicts: python3dist(pytest) = 3.3.0
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(psutil)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm)
BuildRequires:  python3dist(sphinx) >= 1.6.0
BuildRequires:  python3dist(sphinx-bootstrap-theme)
BuildRequires:  python3dist(sphinx)

%description
 python-lz4 Status .. image::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Conflicts:      python3dist(pytest) = 3.3.0
Requires:       python3dist(flake8)
Requires:       python3dist(psutil)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(sphinx) >= 1.6.0
Requires:       python3dist(sphinx-bootstrap-theme)
%description -n python3-%{pypi_name}
 python-lz4 Status .. image::

%package -n python-%{pypi_name}-doc
Summary:        lz4 documentation
%description -n python-%{pypi_name}-doc
Documentation for lz4

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
%license docs/license.rst LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license docs/license.rst LICENSE
