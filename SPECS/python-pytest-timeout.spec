# Created by pyp2rpm-3.3.2
%global pypi_name pytest-timeout

Name:           python-%{pypi_name}
Version:        1.3.3
Release:        %mkrel 1
Summary:        py.test plugin to abort hanging tests
Group:          Development/Python
License:        MIT
URL:            http://bitbucket.org/pytest-dev/pytest-timeout/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest) >= 3.6.0
BuildRequires:  python3dist(setuptools)

%description
 pytest-timeout This is a plugin which will terminate tests after a certain
timeout. When doing so it will show a stack dump of all threads running at the
time. This is useful when running tests under a continuous integration server
or simply if you don't know why the test suite Note that while by default on
POSIX systems py.test will continue to execute the tests after a test has
timed, out...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pytest) >= 3.6.0
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
 pytest-timeout This is a plugin which will terminate tests after a certain
timeout. When doing so it will show a stack dump of all threads running at the
time. This is useful when running tests under a continuous integration server
or simply if you don't know why the test suite Note that while by default on
POSIX systems py.test will continue to execute the tests after a test has
timed, out...


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
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/pytest_timeout.py
%{python3_sitelib}/pytest_timeout-%{version}-py?.?.egg-info
