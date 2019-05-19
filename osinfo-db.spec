Summary:	osinfo database
Summary(pl.UTF-8):	Baza danych osinfo
Name:		osinfo-db
Version:	20190504
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
# Source0-md5:	30dc73bece7ec1ddf8c0d12e535ed025
URL:		https://libosinfo.org/
BuildRequires:	osinfo-db-tools
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines.

%description -l pl.UTF-8
Baza danych osinfo zabiera informacje o systemach operacyjnych oraz
platformach hipernadzorców, ułatwiające automatyczną konfigurację i
zaopatrywanie nowych maszyn wirtualnych.

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
