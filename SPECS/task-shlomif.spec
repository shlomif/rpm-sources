Summary:	Require basic things that Shlomi Fish needs.
Name:		task-shlomif
Version:	0.2.0
Release:	%mkrel 1
License:	BSD
Group:		System
Url:		http://www.shlomifish.org/
BuildArch:	noarch
# Needed for SASL support in postfix - e.g: for mail.shlomifish.org /
# hostgator.com
Requires:   cyrus-sasl
Requires:   postfix
# Needed for SASL support in postfix - e.g: for mail.shlomifish.org /
# hostgator.com
Requires:   lib64sasl2-plug-anonymous
Requires:   lib64sasl2-plug-crammd5
Requires:   lib64sasl2-plug-digestmd5
Requires:   lib64sasl2-plug-gssapi
Requires:   lib64sasl2-plug-ldapdb
Requires:   lib64sasl2-plug-login
Requires:   lib64sasl2-plug-mysql
Requires:   lib64sasl2-plug-ntlm
Requires:   lib64sasl2-plug-otp
Requires:   lib64sasl2-plug-pgsql
Requires:   lib64sasl2-plug-plain
Requires:   lib64sasl2-plug-sasldb
Requires:   lib64sasl2-plug-scram
Requires:   lib64sasl2-plug-sqlite3
Requires:   lib64sasl2-plug-srp
Requires:   lib64sasl2_3
%description
This task package installs some of the packages that Shlomi Fish needs.

%files


%changelog
* Mon Jan 12 2015 shlomif <shlomif@shlomifish.org> 0.2.0-1.mga5
- Initial package.
