Summary:	Multi-threaded SNMP scanner (like a snmpbulkwalk)
Name:		multiwalk2c
Version:	0.2.1
Release:	6
License:	GPLv2+
Group:		System/Servers
Url:		http://wegorz.marton.pl/
Source0:	http://wegorz.marton.pl/%{name}-%{version}.tar.gz
Patch0:		multiwalk2c-0.1.1-compile_fix.diff
BuildRequires:	net-snmp-devel
BuildRequires:	pkgconfig(libcrypto)

%description
multiwalk2c is a multi-threaded SNMP scanner. It is a modified version of
snmpbulkwalk. It can scan agents listed in special agents file, write to a
single or many output files, and traverse different parts of a MIB tree in
one thread.

%files
%doc COPYING README
%{_bindir}/multiwalk2c

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x

%make

%install
%makeinstall_std

