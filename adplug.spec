#
# TODO:
# - why libbinio-static?
#
Summary:	AdLib sound player library
Summary(pl):	Biblioteka odtwarzacza d¼wiêku AdLib
Name:		adplug
Version:	1.5.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
# Source0-md5:	95d62805cff551bed84298e737a26df9
URL:		http://adplug.sourceforge.net/
BuildRequires:	libbinio-devel >= 1.1
BuildRequires:	libbinio-static >= 1.1
Requires:	libbinio >= 1.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound
player library, mainly written in C++. AdPlug plays sound data,
originally created for the AdLib (OPL2) audio board, on top of an OPL2
emulator or by using the real hardware. No OPL2 chip is required for
playback.

%description -l pl
AdPlug to wolnodostêpna, wieloplatformowa, niezale¿na od sprzêtu
biblioteka odtwarzacza d¼wiêku AdLib, napisana g³ównie w C++. AdPlug
odtwarza dane d¼wiêkowe stworzone pierwotnie dla karty d¼wiêkowej
AdLib (OPL2) przy u¿yciu emulatora OPL2 lub prawdziwego sprzêtu. Do
odtwarzania nie jest wymagany uk³ad OPL2.

%package devel
Summary:	Header files for AdPlug library
Summary(pl):	Pliki nag³ówkowe biblioteki AdPlug.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for AdPlug library.

%description devel -l pl
Ten pakiet zawiera pliki nag³ówkowe biblioteki AdPlug.

%package static
Summary:	Static AdPlug library
Summary(pl):	Statyczna biblioteka AdPlug
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static AdPlug library.

%description static -l pl
Statyczna biblioteka AdPlug.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_infodir}/*.info*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
