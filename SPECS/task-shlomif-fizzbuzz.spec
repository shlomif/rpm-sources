Summary:	Require deps that the fizzbuzz tests need
Name:		task-shlomif-fizzbuzz
Version:	0.0.1
Release:	%mkrel 1
License:	BSD
Group:		System
Url:		https://github.com/shlomif/fizz-buzz
BuildArch:	noarch
Requires:   hugs98
Requires:   ocaml
Requires:   php-cli
Requires:   zsh
%description
This task package installs some of the packages that fizzbuzz needs.

%files


%changelog
* Mon Jan 12 2015 shlomif <shlomif@shlomifish.org> 0.2.0-1.mga5
- Initial package.
