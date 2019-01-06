# Created by pyp2rpm-3.3.2
%global pypi_name reno

Name:           python-%{pypi_name}
Version:        2.11.2
Release:        %mkrel 1
Summary:        RElease NOtes manager
Group:          Development/Python
License:        None
URL:            https://docs.openstack.org/reno/latest/
Source0:        https://files.pythonhosted.org/packages/source/r/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(hacking) = 0.13.0
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(docutils) >= 0.11
BuildRequires:  python3dist(dulwich) >= 0.15.0
BuildRequires:  python3dist(hacking) >= 0.12.0
BuildRequires:  python3dist(mock) >= 1.2
BuildRequires:  python3dist(openstackdocstheme) >= 1.11.0
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(pbr)
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(pyyaml) >= 3.10
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9.0
BuildRequires:  python3dist(sphinx) >= 1.6.1
BuildRequires:  python3dist(testrepository) >= 0.0.18
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testtools) >= 1.4.0
BuildRequires:  python3dist(sphinx)

%description
 reno: A New Way to Manage Release Notes Reno is a release notes manager
designed with high throughput in mind, supporting fast distributed development
teams without introducing additional development processes. Our goal is to
encourage detailed and accurate release notes for every release.Reno uses git
to store its data, along side the code being described. This means release
notes can be...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(docutils) >= 0.11
Requires:       python3dist(dulwich) >= 0.15.0
Requires:       python3dist(pbr)
Requires:       python3dist(pyyaml) >= 3.10
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.9.0
Requires:       python3dist(sphinx) >= 1.6.1
%description -n python3-%{pypi_name}
 reno: A New Way to Manage Release Notes Reno is a release notes manager
designed with high throughput in mind, supporting fast distributed development
teams without introducing additional development processes. Our goal is to
encourage detailed and accurate release notes for every release.Reno uses git
to store its data, along side the code being described. This means release
notes can be...

%package -n python-%{pypi_name}-doc
Summary:        reno documentation
%description -n python-%{pypi_name}-doc
Documentation for reno

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/reno
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
