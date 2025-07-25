Name:           perl-File-ShouldUpdate
Version:        0.2.1
Release:        1%{?dist}
Summary:        Determine if files should be updated using make-like syntax
License:        MIT
URL:            https://metacpan.org/dist/File-ShouldUpdate
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-ShouldUpdate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6.0
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(parent)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(blib)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%description
This module provides should_update() and should_update_multi() which can be
used to determine if files should be updated based on the mtime timestamps
of their dependencies. They avoid confusing between targets and
dependencies by using the syntactic sugar of the familiar makefile rules (
https://en.wikipedia.org/wiki/Make_(software) ).

%prep
%setup -q -n File-ShouldUpdate-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/File/
%{_mandir}/man3/File::ShouldUpdate.3pm*

%changelog
* Thu Jul 17 2025 Shlomi Fish <shlomif@shlomifish.org> 0.2.1-1
- Specfile autogenerated by cpanspec 1.78.
