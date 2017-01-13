Summary:	osinfo database
Name:		osinfo-db
Version:	20170107
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
# Source0-md5:	c1e5cda4155b80401acd4e8265283fe9
URL:		https://libosinfo.org/
BuildRequires:	osinfo-db-tools
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines.

%install
rm -rf $RPM_BUILD_ROOT

osinfo-db-import \
	--root $RPM_BUILD_ROOT \
	--dir %{_datadir}/osinfo \
	%{SOURCE0}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/osinfo

