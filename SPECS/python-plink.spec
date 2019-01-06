# Created by pyp2rpm-3.3.2
%global pypi_name plink

Name:           python-%{pypi_name}
Version:        2.2
Release:        %mkrel 1
Summary:        A full featured Tk-based knot and link editor
Group:          Development/Python
License:        GPLv2+
URL:            http://www.math.uic.edu/t3m/plink/doc/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
PLink is a full featured graphical editor for knot and link projections, using
the cross-platform GUI toolkit Tk. The primary focus is on piecewise-linear
link projections, but it also supports a "smooth mode" and can export images in
PostScript, PDF, SVG, and TikZ formats. See the PLink home page < for complete
details.This is a pure Python module and you can install it via either pip <
or...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(future)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
PLink is a full featured graphical editor for knot and link projections, using
the cross-platform GUI toolkit Tk. The primary focus is on piecewise-linear
link projections, but it also supports a "smooth mode" and can export images in
PostScript, PDF, SVG, and TikZ formats. See the PLink home page < for complete
details.This is a pure Python module and you can install it via either pip <
or...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%{_bindir}/plink
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
