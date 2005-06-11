#
# TODO:
# - proper Group
#
Summary:	AdLib sound player library
Name:		adplug
Version:	1.5
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
# Source0-md5:	376f23f5e50ef47435c7f6e7c5319429
URL:		http://adplug.sourceforge.net/
BuildRequires:	libbinio-devel >= 1.1
BuildRequires:	libbinio-static >= 1.1
Requires:	libbinio >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

%package devel
Summary:	Development libraries and header files for termcap library
Group:		Development/Libraries

%description devel
This is the package containing the development libaries and header
files for adplug.

%description -l pl
Ten apkiet zawiera biblioteki deweloperskie i pliki nag³ówkowe dla adplug.

%package static
Summary:	Static adplug library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static adplug library.

%description -l pl
Statyczna biblioteka dla adplug.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so*
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
