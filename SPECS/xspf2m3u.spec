%define upstream_name    App-xspf2m3u
%define upstream_version 0.0.1

%{?perl_default_filter}

Name:       xspf2m3u
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Convert .xspf playlists to .m3u ones
License:    GPLv1+ or Artistic
Group:      Video/Utilities
Url:        http://metacpan.org/release/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App::Cmd::Setup)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Handle)
BuildRequires: perl(IPC::Open3)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Path::Tiny)
BuildRequires: perl(Test::More)
BuildRequires: perl(XML::XSPF)
BuildRequires: perl(autodie)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(Module::Build)
BuildArch: noarch

%description
A command line tool to convert .xspf playlists to .m3u ones.
(For use by mpv and similar media players).


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*
%{_bindir}/xspf2m3u
%{_mandir}/man1/xspf2m3u.1.*

%changelog
* Tue Dec 17 2019 cpan2dist 0.0.1-1mga
- initial mageia release, generated with cpan2dist
