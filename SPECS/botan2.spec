%global major_version 4
%define dlname Botan
%define botan2 2

Name:           botan2
Version:        2.4.0
Release:        %mkrel 1
Summary:        Crypto and TLS for C++11
Group:          System/Libraries
License:        BSD
URL:            https://botan.randombit.net/
Source0:        https://botan.randombit.net/releases/%{dlname}-%{version}.tgz#!/%{name}-%{version}.tgz
Patch0:         01-remove-rpath-gcc.patch
Patch1:         02-fix-wrong-script-interpreter.patch

BuildRequires:  gcc-c++
BuildRequires:  python
BuildRequires:  python-sphinx
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
Requires:       python3

%description
Botan is a BSD-licensed crypto library written in C++. It provides a
wide variety of basic cryptographic algorithms, X.509 certificates and
CRLs, PKCS \#10 certificate requests, a filter/pipe message processing
system, and a wide variety of other features, all written in portable
C++. The API reference, tutorial, and examples may help impart the
flavor of the library. This is the current stable release branch 2.x
of Botan.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
%{summary}

This package contains HTML documentation for %{name}.


%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}
%{summary}

This package contains the Python3 binding for %{name}.


%prep
%setup -q -n %{dlname}-%{version}
%patch0 -p0
%patch1 -p0

%build
# we have the necessary prerequisites, so enable optional modules
%global enable_modules bzip2,zlib,openssl

./configure.py \
        --prefix=%{_prefix} \
        --libdir=%{_lib} \
        --docdir=%{_docdir} \
        --cc=gcc \
        --os=linux \
        --cpu=%{_arch} \
        --enable-modules=%{enable_modules} \
        --with-python-version=%{python3_version} \
        --with-sphinx \
        --with-debug-info

%make_build

%install
make install \
     DESTDIR=%{buildroot} \
     INSTALL_CMD_EXEC="install -p -m 755" \
     INSTALL_CMD_DATA="install -p -m 644"

chmod 755 %{buildroot}%{python3_sitearch}/botan2.py

%files
%license license.txt
%{_docdir}/
%{_libdir}/libbotan-%{botan2}.so.%{major_version}{,.*}
%{_bindir}/botan
%{_mandir}/man1/

%files devel
%license license.txt
%{_includedir}/
%exclude %{_libdir}/libbotan-%{botan2}.a
%{_libdir}/libbotan-%{botan2}.so
%{_libdir}/pkgconfig/botan-%{botan2}.pc

%files doc
%license license.txt
%{_docdir}/

%files -n python3-%{name}
%license license.txt
%{python3_sitearch}/%{name}.py
%{python3_sitearch}/__pycache__/

%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./botan-test

