# Created by pyp2rpm-3.3.2
%global pypi_name spherogram

Name:           python-%{pypi_name}
Version:        1.8.1
Release:        %mkrel 1
Summary:        Spherical diagrams for 3-manifold topology
Group:          Development/Python
License:        GPLv2+
URL:            https://bitbucket.org/t3m/spherogram
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(networkx) >= 1.3
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(snappy-manifolds) >= 1.0

%description
Spherogram is a Python module for dealing with the kind of planar diagrams that
arise in 3-dimensional topology, such as link and Heegaard diagrams. It a
component of the larger SnapPy <>_ project. For some basic examples of using
Spherogram to build links, see here < You can browse the source code <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(decorator)
Requires:       python3dist(future)
Requires:       python3dist(networkx) >= 1.3
Requires:       python3dist(snappy-manifolds) >= 1.0
%description -n python3-%{pypi_name}
Spherogram is a Python module for dealing with the kind of planar diagrams that
arise in 3-dimensional topology, such as link and Heegaard diagrams. It a
component of the larger SnapPy <>_ project. For some basic examples of using
Spherogram to build links, see here < You can browse the source code <


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
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
