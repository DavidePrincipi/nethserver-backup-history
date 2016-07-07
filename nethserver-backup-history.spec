Summary: NethServer backup config files history
Name: nethserver-backup-history
Version: 0.0.0
Release: 1%{?dist}
License: GPL
Group: System
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: nethserver-devtools, gettext
Requires: nethserver-base

%description
NethServer backup config history

%prep
%setup

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
rm -f %{name}-%{version}-%{release}-filelist
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist 
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
