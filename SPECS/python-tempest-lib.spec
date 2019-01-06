# Created by pyp2rpm-3.3.2
%global pypi_name tempest-lib

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        %mkrel 1
Summary:        OpenStack Functional Testing Library
Group:          Development/Python
License:        Apache License, Version 2.0
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(jsonschema) = 2.5.0
BuildConflicts: python3dist(oslosphinx) = 3.4.0
BuildConflicts: python3dist(sphinx) = 1.2.0
BuildConflicts: python3dist(sphinx) = 1.3b1
BuildRequires:  python3dist(babel) >= 1.3
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(ddt) >= 1.0.1
BuildRequires:  python3dist(discover)
BuildRequires:  python3dist(fixtures) >= 1.3.1
BuildRequires:  python3dist(hacking) < 0.11
BuildRequires:  python3dist(hacking) >= 0.10.0
BuildRequires:  python3dist(httplib2) >= 0.7.5
BuildRequires:  python3dist(iso8601) >= 0.1.9
BuildRequires:  python3dist(jsonschema) < 3.0.0
BuildRequires:  python3dist(jsonschema) >= 2.0.0
BuildRequires:  python3dist(mock) >= 1.2
BuildRequires:  python3dist(os-testr) >= 0.4.1
BuildRequires:  python3dist(oslo.log) >= 1.14.0
BuildRequires:  python3dist(oslosphinx) >= 2.5.0
BuildRequires:  python3dist(oslotest) >= 1.10.0
BuildRequires:  python3dist(paramiko) >= 1.16.0
BuildRequires:  python3dist(pbr) >= 1.6
BuildRequires:  python3dist(pbr) >= 1.8
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(reno) >= 0.1.1
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9.0
BuildRequires:  python3dist(sphinx) < 1.3
BuildRequires:  python3dist(sphinx) >= 1.1.2
BuildRequires:  python3dist(testrepository) >= 0.0.18
BuildRequires:  python3dist(testscenarios) >= 0.4
BuildRequires:  python3dist(testtools) >= 1.4.0
BuildRequires:  python3dist(sphinx)

%description
 tempest-lib OpenStack Functional Testing Library* Free software: Apache
license * Documentation: * Source: * Bugs: is a library of common functionality
that was originally in tempest (or similar in scope to tempest)**As of the
1.0.0 release tempest-lib as a separate repository and project is deprecated.
The library now exists as part of the tempest project, all future development
will occur...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Conflicts:      python3dist(jsonschema) = 2.5.0
Requires:       python3dist(babel) >= 1.3
Requires:       python3dist(fixtures) >= 1.3.1
Requires:       python3dist(httplib2) >= 0.7.5
Requires:       python3dist(iso8601) >= 0.1.9
Requires:       python3dist(jsonschema) < 3.0.0
Requires:       python3dist(jsonschema) >= 2.0.0
Requires:       python3dist(os-testr) >= 0.4.1
Requires:       python3dist(oslo.log) >= 1.14.0
Requires:       python3dist(paramiko) >= 1.16.0
Requires:       python3dist(pbr) >= 1.6
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.9.0
%description -n python3-%{pypi_name}
 tempest-lib OpenStack Functional Testing Library* Free software: Apache
license * Documentation: * Source: * Bugs: is a library of common functionality
that was originally in tempest (or similar in scope to tempest)**As of the
1.0.0 release tempest-lib as a separate repository and project is deprecated.
The library now exists as part of the tempest project, all future development
will occur...

%package -n python-%{pypi_name}-doc
Summary:        tempest-lib documentation
%description -n python-%{pypi_name}-doc
Documentation for tempest-lib

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
%doc doc/source/readme.rst README.rst
%{_bindir}/check-uuid
%{_bindir}/skip-tracker
%{python3_sitelib}/tempest_lib
%{python3_sitelib}/tempest_lib-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
