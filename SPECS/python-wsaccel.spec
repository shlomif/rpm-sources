# Created by pyp2rpm-3.3.2
%global pypi_name wsaccel

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        %mkrel 1
Summary:        Accelerator for ws4py and AutobahnPython
Group:          Development/Python
License:        Apache
URL:            https://github.com/methane/wsaccel
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
WSAccell is WebSocket accelerator for AutobahnPython < ws4py < and Tornado <
replaces per-byte process in them with Cython version.AutobahnPython beginning
with version 0.6 automatically uses WSAccell if available. Otherwise you can
run-time patch supported WebSocket libraries using:.. code-block:: python
import wsaccel wsaccel.patch_autobahn() for autobahn. wsaccel.patch_ws4py() for
ws4py....

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
WSAccell is WebSocket accelerator for AutobahnPython < ws4py < and Tornado <
replaces per-byte process in them with Cython version.AutobahnPython beginning
with version 0.6 automatically uses WSAccell if available. Otherwise you can
run-time patch supported WebSocket libraries using:.. code-block:: python
import wsaccel wsaccel.patch_autobahn() for autobahn. wsaccel.patch_ws4py() for
ws4py....


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info
