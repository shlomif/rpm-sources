# Created by pyp2rpm-3.3.2
%global pypi_name pypng

Name:           python-%{pypi_name}
Version:        0.0.19
Release:        %mkrel 1
Summary:        Pure Python PNG image encoder/decoder
Group:          Development/Python
License:        None
URL:            https://github.com/drj11/pypng
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
PyPNG allows PNG image files to be read and written using pure Python.It's
available from github.com is kindly hosted by PyPI (and also available in the
download tarball).

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyPNG allows PNG image files to be read and written using pure Python.It's
available from github.com is kindly hosted by PyPI (and also available in the
download tarball).


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
%doc README.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/png.py
%{python3_sitelib}/pngsuite.py
%{python3_sitelib}/test_png.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
