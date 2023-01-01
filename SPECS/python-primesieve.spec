# Created by pyp2rpm-3.3.8
%global pypi_name primesieve
%global pypi_version 2.3.2

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python bindings for primesieve

License:        MIT
URL:            https://github.com/kimwalisch/primesieve-python
Source0:        %{pypi_source}

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(primesieve)
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 primesieve-python[![Build Status]( [![PyPI]( SummaryPython bindings for the
[primesieve]( C++ library.Generates primes orders of magnitude faster than any
pure Python code!**Features:*** Get an array of primes * Iterate over primes
using little memory * Find the nth prime * Count/print primes and [prime
k-tuplets]( * Multi-threaded for counting primes and finding the nth prime

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 primesieve-python[![Build Status]( [![PyPI]( SummaryPython bindings for the
[primesieve]( C++ library.Generates primes orders of magnitude faster than any
pure Python code!**Features:*** Get an array of primes * Iterate over primes
using little memory * Find the nth prime * Count/print primes and [prime
k-tuplets]( * Multi-threaded for counting primes and finding the nth prime


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Sat Dec 31 2022 Shlomi Fish <shlomif@shlomifish.org> - 2.3.1-1
- Initial package.
