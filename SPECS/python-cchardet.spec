# Created by pyp2rpm-3.3.2
%global pypi_name cchardet

Name:           python-%{pypi_name}
Version:        2.1.4
Release:        %mkrel 1
Summary:        cChardet is high speed universal character encoding detector
Group:          Development/Python
License:        Mozilla Public License
URL:            https://github.com/PyYoshi/cChardet
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
cChardet is high speed universal character encoding detector. - binding to
uchardet_. Supported Languages/Encodings International (Unicode)

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
cChardet is high speed universal character encoding detector. - binding to
uchardet_. Supported Languages/Encodings International (Unicode)


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst src/ext/uchardet/README.md src/ext/uchardet/doc/README.maintainer
%{_bindir}/cchardetect
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
