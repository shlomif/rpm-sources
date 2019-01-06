# Created by pyp2rpm-3.3.2
%global pypi_name pyqrcode

Name:           python-%{pypi_name}
Version:        1.2.1
Release:        %mkrel 1
Summary:        A QR code generator written purely in Python with SVG, EPS, PNG and terminal output
Group:          Development/Python
License:        BSD
URL:            https://github.com/mnooner256/pyqrcode
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PyQRCode-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
========
PyQRCode
========

.. contents::

The pyqrcode module is a QR code
generator that is simple to use and written
in pure python. The module can
automates most of the building process for
creating QR codes. Most codes can be
created using only two lines of code!

Unlike other generators, all of the
helpers can be controlled manually. You are
free to set any or all of the
properties of...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pypng) >= 0.0.13
%description -n python3-%{pypi_name}
========
PyQRCode
========

.. contents::

The pyqrcode module is a QR code
generator that is simple to use and written
in pure python. The module can
automates most of the building process for
creating QR codes. Most codes can be
created using only two lines of code!

Unlike other generators, all of the
helpers can be controlled manually. You are
free to set any or all of the
properties of...


%prep
%autosetup -n PyQRCode-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/PyQRCode-%{version}-py?.?.egg-info
