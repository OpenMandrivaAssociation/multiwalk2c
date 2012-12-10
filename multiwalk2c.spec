Summary:	Multi-threaded SNMP scanner (like a snmpbulkwalk)
Name:		multiwalk2c
Version:	0.2.1
Release:	%mkrel 4
License:	GPL
Group:		System/Servers
URL:		http://wegorz.marton.pl/
Source0:	http://wegorz.marton.pl/%{name}-%{version}.tar.gz
Patch0:		multiwalk2c-0.1.1-compile_fix.diff
BuildRequires:	net-snmp-devel
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}buildroot

%description
multiwalk2c is a multi-threaded SNMP scanner. It is a modified version of
snmpbulkwalk. It can scan agents listed in special agents file, write to a
single or many output files, and traverse different parts of a MIB tree in
one thread.

%prep

%setup -q
%patch0 -p0

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --copy --add-missing --foreign

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/multiwalk2c


%changelog
* Mon Jul 18 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-4mdv2011
+ Revision: 690294
- rebuilt against new net-snmp libs

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-3mdv2011.0
+ Revision: 627808
- don't force the usage of automake1.7

* Tue Oct 12 2010 Funda Wang <fwang@mandriva.org> 0.2.1-2mdv2011.0
+ Revision: 585066
- rebuild

* Mon Aug 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.1-1mdv2011.0
+ Revision: 568090
- 0.2.1

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdv2010.0
+ Revision: 457692
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2010.0
+ Revision: 430123
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 253361
- rebuild

* Fri Mar 07 2008 Oden Eriksson <oeriksson@mandriva.com> 0.2-1mdv2008.1
+ Revision: 181233
- 0.2

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.2-1mdv2008.0
+ Revision: 60414
- 0.1.2
- Import multiwalk2c



* Wed Aug 08 2007 Oden Eriksson <oeriksson@mandriva.com> 0.1.1-1mdv2008.0
- initial Mandriva package
