# Created by pyp2rpm-3.3.2
%global pypi_name sqlalchemy-migrate

Name:           python-%{pypi_name}
Version:        0.11.0
Release:        %mkrel 1
Summary:        Database schema migration for SQLAlchemy
Group:          Development/Python
License:        None
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildConflicts: python3dist(sqlalchemy) = 0.9.5
BuildRequires:  python3dist(coverage) >= 3.6
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(discover)
BuildRequires:  python3dist(feedparser)
BuildRequires:  python3dist(fixtures) >= 0.3.14
BuildRequires:  python3dist(hacking) < 0.11
BuildRequires:  python3dist(hacking) >= 0.10.0
BuildRequires:  python3dist(mock) >= 1.2
BuildRequires:  python3dist(mox) >= 0.5.3
BuildRequires:  python3dist(pbr) >= 1.3
BuildRequires:  python3dist(pbr) >= 1.8
BuildRequires:  python3dist(pep8) = 1.5.7
BuildRequires:  python3dist(psycopg2)
BuildRequires:  python3dist(pyflakes) = 0.8.1
BuildRequires:  python3dist(pylint)
BuildRequires:  python3dist(python-subunit) >= 0.0.18
BuildRequires:  python3dist(pytz) >= 2010h
BuildRequires:  python3dist(scripttest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.7.0
BuildRequires:  python3dist(sphinx) >= 1.1.2
BuildRequires:  python3dist(sphinxcontrib-issuetracker)
BuildRequires:  python3dist(sqlalchemy) >= 0.7.8
BuildRequires:  python3dist(sqlparse)
BuildRequires:  python3dist(tempest-lib) >= 0.1.0
BuildRequires:  python3dist(tempita) >= 0.4
BuildRequires:  python3dist(testrepository) >= 0.0.17
BuildRequires:  python3dist(testtools) < 0.9.36
BuildRequires:  python3dist(testtools) >= 0.9.34
BuildRequires:  python3dist(sphinx)

%description
sqlalchemy-migrate Fork from to get it working with SQLAlchemy 0.8.Inspired by
Ruby on Rails' migrations, Migrate provides a way to deal with database schema
changes in SQLAlchemy <>_ projects.Migrate extends SQLAlchemy to have database
changeset handling. It provides a database change repository mechanism which
can be used from the command line as well as from inside python code.Help
Sphinx...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Conflicts:      python3dist(sqlalchemy) = 0.9.5
Requires:       python3dist(decorator)
Requires:       python3dist(pbr) >= 1.8
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.7.0
Requires:       python3dist(sqlalchemy) >= 0.7.8
Requires:       python3dist(sqlparse)
Requires:       python3dist(tempita) >= 0.4
%description -n python3-%{pypi_name}
sqlalchemy-migrate Fork from to get it working with SQLAlchemy 0.8.Inspired by
Ruby on Rails' migrations, Migrate provides a way to deal with database schema
changes in SQLAlchemy <>_ projects.Migrate extends SQLAlchemy to have database
changeset handling. It provides a database change repository mechanism which
can be used from the command line as well as from inside python code.Help
Sphinx...

%package -n python-%{pypi_name}-doc
Summary:        sqlalchemy-migrate documentation
%description -n python-%{pypi_name}-doc
Documentation for sqlalchemy-migrate

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
%doc README.rst
%{_bindir}/migrate
%{_bindir}/migrate-repository
%{python3_sitelib}/migrate
%{python3_sitelib}/sqlalchemy_migrate-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
