# Created by pyp2rpm-3.3.2
%global pypi_name snappy

Name:           python-%{pypi_name}
Version:        2.7
Release:        %mkrel 1
Summary:        Studying the topology and geometry of 3-manifolds, with a focus on hyperbolic structures
Group:          Development/Python
License:        GPLv2+
URL:            http://snappy.computop.org
Source0:        https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cypari) >= 2.2
BuildRequires:  python3dist(decorator)
BuildRequires:  python3dist(future)
BuildRequires:  python3dist(fxrays) >= 1.3
BuildRequires:  python3dist(ipython) >= 0.13
BuildRequires:  python3dist(plink) >= 2.2
BuildRequires:  python3dist(pypng)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(snappy-manifolds) >= 1.0
BuildRequires:  python3dist(spherogram) >= 1.8.1

%description
SnapPy is a package for studying the topology and geometry of 3-manifolds, with
a focus on hyperbolic structures. It is based on the SnapPea kernel written by
Jeff Weeks <>_. Complete documentation is available on the web including the
main page <>_ and an installation guide < You can also browse the source code <

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(cypari) >= 2.2
Requires:       python3dist(decorator)
Requires:       python3dist(future)
Requires:       python3dist(fxrays) >= 1.3
Requires:       python3dist(ipython) >= 0.13
Requires:       python3dist(plink) >= 2.2
Requires:       python3dist(pypng)
Requires:       python3dist(setuptools)
Requires:       python3dist(snappy-manifolds) >= 1.0
Requires:       python3dist(spherogram) >= 1.8.1
%description -n python3-%{pypi_name}
SnapPy is a package for studying the topology and geometry of 3-manifolds, with
a focus on hyperbolic structures. It is based on the SnapPea kernel written by
Jeff Weeks <>_. Complete documentation is available on the web including the
main page <>_ and an installation guide < You can also browse the source code <


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
%license python/togl/darwin-tk8.4/Togl2.0/LICENSE python/togl/linux2-x86_64-tk8.5/Togl2.0/LICENSE python/togl/win32VC-tk8.5/Togl2.1/LICENSE python/togl/linux2-x86_64-tk8.4/Togl2.0/LICENSE python/togl/win32VC-x86_64-tk8.6/Togl2.1/LICENSE python/togl/darwin-tk8.7/Togl2.1/LICENSE python/togl/linux2-tk8.5/Togl2.0/LICENSE python/togl/linux2-x86_64-tk8.6/Togl2.0/LICENSE python/togl/win32VC-x86_64-tk8.5/Togl2.1/LICENSE python/togl/win32-tk8.5/Togl2.0/LICENSE python/togl/darwin-tk8.6/Togl2.1/LICENSE python/togl/linux2-tk8.6/Togl2.0/LICENSE python/togl/linux2-tk8.4/Togl2.0/LICENSE python/togl/win32VC-tk8.6/Togl2.1/LICENSE python/togl/darwin-tk8.5/Togl2.1/LICENSE
%doc README.rst
%{_bindir}/SnapPy
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/snappy/dev
%{python3_sitearch}/snappy/manifolds
%{python3_sitearch}/snappy/ptolemy
%{python3_sitearch}/snappy/snap
%{python3_sitearch}/snappy/snap/peripheral
%{python3_sitearch}/snappy/snap/t3mlite
%{python3_sitearch}/snappy/togl
%{python3_sitearch}/snappy/twister
%{python3_sitearch}/snappy/verify
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
