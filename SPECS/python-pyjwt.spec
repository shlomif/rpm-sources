# Created by pyp2rpm-3.3.2
%global pypi_name pyjwt

Name:           python-%{pypi_name}
Version:        1.7.1
Release:        %mkrel 1
Summary:        JSON Web Token implementation in Python
Group:          Development/Python
License:        MIT
URL:            http://github.com/jpadilla/pyjwt
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PyJWT-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography) >= 1.4
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(flake8-import-order)
BuildRequires:  python3dist(pep8-naming)
BuildRequires:  python3dist(pytest) < 5.0.0
BuildRequires:  python3dist(pytest) < 5.0.0
BuildRequires:  python3dist(pytest) >= 4.0.1
BuildRequires:  python3dist(pytest) >= 4.0.1
BuildRequires:  python3dist(pytest-cov) < 3.0.0
BuildRequires:  python3dist(pytest-cov) < 3.0.0
BuildRequires:  python3dist(pytest-cov) >= 2.6.0
BuildRequires:  python3dist(pytest-cov) >= 2.6.0
BuildRequires:  python3dist(pytest-runner) < 5.0.0
BuildRequires:  python3dist(pytest-runner) < 5.0.0
BuildRequires:  python3dist(pytest-runner) >= 4.2
BuildRequires:  python3dist(pytest-runner) >= 4.2
BuildRequires:  python3dist(setuptools)

%description
 A Python implementation of RFC 7519 < Original implementation was written by
@progrium <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(cryptography) >= 1.4
Requires:       python3dist(flake8)
Requires:       python3dist(flake8-import-order)
Requires:       python3dist(pep8-naming)
Requires:       python3dist(pytest) < 5.0.0
Requires:       python3dist(pytest) >= 4.0.1
Requires:       python3dist(pytest-cov) < 3.0.0
Requires:       python3dist(pytest-cov) >= 2.6.0
Requires:       python3dist(pytest-runner) < 5.0.0
Requires:       python3dist(pytest-runner) >= 4.2
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 A Python implementation of RFC 7519 < Original implementation was written by
@progrium <


%prep
%autosetup -n PyJWT-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/pyjwt
%{python3_sitelib}/jwt
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
