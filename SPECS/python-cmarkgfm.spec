# Created by pyp2rpm-3.3.2
%global pypi_name cmarkgfm

Name:           python-%{pypi_name}
Version:        0.4.2
Release:        %mkrel 1
Summary:        Minimal bindings to GitHub's fork of cmark
Group:          Development/Python
License:        None
URL:            https://github.com/jonparrott/cmarkgfm
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.0.0
BuildRequires:  python3dist(cffi) >= 1.0.0
BuildRequires:  python3dist(setuptools)

%description
cmarkgfm - Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of
cmark.Installation This package is published as cmarkgfm < and can be installed
with pip or pipenv:: pip install --user cmarkgfm pipenv install cmarkgfmWheels
are provided for macOS, Linux, and Windows for Python 2.7, 3.4, 3.5, and
3.6.Usage High-level usage is really straightforward. To render normal
CommonMark...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(cffi) >= 1.0.0
%description -n python3-%{pypi_name}
cmarkgfm - Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of
cmark.Installation This package is published as cmarkgfm < and can be installed
with pip or pipenv:: pip install --user cmarkgfm pipenv install cmarkgfmWheels
are provided for macOS, Linux, and Windows for Python 2.7, 3.4, 3.5, and
3.6.Usage High-level usage is really straightforward. To render normal
CommonMark...


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
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
