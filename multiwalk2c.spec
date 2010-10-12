Summary:	Multi-threaded SNMP scanner (like a snmpbulkwalk)
Name:		multiwalk2c
Version:	0.2.1
Release:	%mkrel 2
License:	GPL
Group:		System/Servers
URL:		http://wegorz.marton.pl/
Source0:	http://wegorz.marton.pl/%{name}-%{version}.tar.gz
Patch0:		multiwalk2c-0.1.1-compile_fix.diff
BuildRequires:	net-snmp-devel
BuildRequires:	automake1.7
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
libtoolize --copy --force; aclocal-1.7; autoconf; automake-1.7 --copy --add-missing --foreign

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
