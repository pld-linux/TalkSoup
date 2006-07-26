Summary:	IRC for GNUstep
Summary(pl):	Program do IRC dla GNUstepa
Name:		TalkSoup
Version:	0.81
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://www.linuks.mine.nu/andy/files/talksoup/%{name}-%{version}.tar.gz
# Source0-md5:	5b0671a5d6ea227ba0ccef495052763e
Patch0:		%{name}-initializeWithArguments.patch
URL:		http://www.linuks.mine.nu/andy/talksoup/
BuildRequires:	gnustep-gui-devel >= 0.8.7
Requires:	gnustep-gui >= 0.8.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		libcombo	gnu-gnu-gnu
%define		gsos		linux-gnu
%ifarch %{ix86}
%define		gscpu		ix86
%else
# also s/alpha.*/alpha/, but we use only "alpha" arch for now
%define		gscpu		%{_target_cpu}
%endif
%define		gstriple	%{gscpu}/%{gsos}/%{libcombo}
%define		appdir		%{_libdir}/GNUstep/System/Applications/%{name}.app
%define		supportdir	%{_libdir}/GNUstep/System/Library/ApplicationSupport/%{name}

%description
TalkSoup is a simple IRC client for GNUstep.

%description -l pl
TalkSoup jest prostym klientem IRC dla GNUstepa.

%package devel
Summary:	Headers and framework for IRC apps
Summary(pl):	Pliki nag³ówkowe i struktura dla aplikacji IRC
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
TalkSoup framework and headers for IRC apps.

%description devel -l pl
Struktura i pliki nag³ówkowe TalkSoup dla aplikacji IRC.

%prep
%setup -q
%patch0 -p1

%build
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh
%{__make} \
	OPTFLAG="%{rpmcflags}" \
	messages=yes

%install
rm -rf $RPM_BUILD_ROOT
. %{_libdir}/GNUstep/System/Library/Makefiles/GNUstep.sh

%{__make} install \
	GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{_libdir}/GNUstep/System

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{appdir}
%dir %{supportdir}
%attr(755,root,root) %{supportdir}/*/*/%{gstriple}/*
%{supportdir}/*/*/Resources/*
%attr(755,root,root) %{appdir}/%{name}
%dir %{appdir}/Resources
%{appdir}/Resources/*.desktop
%{appdir}/Resources/*.plist
%{appdir}/Resources/English.lproj
#%{appdir}/Resources/Scripts
%dir %{appdir}/%{gscpu}
%dir %{appdir}/%{gscpu}/%{gsos}
%dir %{appdir}/%{gscpu}/%{gsos}/%{libcombo}
%attr(755,root,root) %{appdir}/%{gstriple}/%{name}
%{appdir}/%{gstriple}/*.openapp
%attr(755,root,root) %{_libdir}/GNUstep/System/Library/Libraries/%{gstriple}/*

%files devel
%defattr(644,root,root,755)
%{_libdir}/GNUstep/System/Library/Headers/*
%{_libdir}/GNUstep/System/Library/Frameworks/*
