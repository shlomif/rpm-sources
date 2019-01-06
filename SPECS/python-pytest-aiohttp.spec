# Created by pyp2rpm-3.3.2
%global pypi_name pytest-aiohttp

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %mkrel 1
Summary:        pytest plugin for aiohttp support
Group:          Development/Python
License:        Apache 2
URL:            https://github.com/aio-libs/pytest-aiohttp/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
pytest-aiohttp pytest plugin for aiohttp supportThe library allows to use
aiohttp pytest plugin < without need for implicitly loading it like
pytest_plugins 'aiohttp.pytest_plugin'. Just run:.. code-block:: console $ pip
install pytest-aiohttpand write tests with the plugin support:.. code-block::
python from aiohttp import web async def hello(request): return
web.Response(bodyb'Hello, world')...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(aiohttp) >= 2.3.5
Requires:       python3dist(pytest)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
pytest-aiohttp pytest plugin for aiohttp supportThe library allows to use
aiohttp pytest plugin < without need for implicitly loading it like
pytest_plugins 'aiohttp.pytest_plugin'. Just run:.. code-block:: console $ pip
install pytest-aiohttpand write tests with the plugin support:.. code-block::
python from aiohttp import web async def hello(request): return
web.Response(bodyb'Hello, world')...


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
%{python3_sitelib}/pytest_aiohttp
%{python3_sitelib}/pytest_aiohttp-%{version}-py?.?.egg-info
