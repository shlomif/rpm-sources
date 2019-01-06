# Created by pyp2rpm-3.3.2
%global pypi_name aiodns

Name:           python-%{pypi_name}
Version:        1.1.1
Release:        %mkrel 1
Summary:        Simple DNS resolver for asyncio
Group:          Development/Python
License:        None
URL:            http://github.com/saghul/aiodns
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Simple DNS resolver for asyncio aiodns provides a simple way for doing
asynchronous DNS resolutions with a synchronous looking interface by using
pycares < import asyncio import aiodns loop asyncio.get_event_loop() resolver
aiodns.DNSResolver(looploop) f resolver.query('google.com','A') result
loop.run_until_complete(f) print(result) The following query types are
supported: A, AAAA, CNAME,...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pycares) >= 1.0.0
%description -n python3-%{pypi_name}
 Simple DNS resolver for asyncio aiodns provides a simple way for doing
asynchronous DNS resolutions with a synchronous looking interface by using
pycares < import asyncio import aiodns loop asyncio.get_event_loop() resolver
aiodns.DNSResolver(looploop) f resolver.query('google.com','A') result
loop.run_until_complete(f) print(result) The following query types are
supported: A, AAAA, CNAME,...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
