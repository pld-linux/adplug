Summary:	AdLib sound player library
Summary(pl.UTF-8):	Biblioteka odtwarzacza dźwięku AdLib
Name:		adplug
Version:	2.3.3
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/adplug/adplug/releases/download/adplug-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	35cb5005c512821ff480c10b43bba270
Patch0:		%{name}-info.patch
URL:		https://adplug.github.io
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake >= 1:1.14
BuildRequires:	libbinio-devel >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	texinfo
Requires:	libbinio >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound
player library, mainly written in C++. AdPlug plays sound data,
originally created for the AdLib (OPL2) audio board, on top of an OPL2
emulator or by using the real hardware. No OPL2 chip is required for
playback.

%description -l pl.UTF-8
AdPlug to wolnodostępna, wieloplatformowa, niezależna od sprzętu
biblioteka odtwarzacza dźwięku AdLib, napisana głównie w C++. AdPlug
odtwarza dane dźwiękowe stworzone pierwotnie dla karty dźwiękowej
AdLib (OPL2) przy użyciu emulatora OPL2 lub prawdziwego sprzętu. Do
odtwarzania nie jest wymagany układ OPL2.

%package devel
Summary:	Header files for AdPlug library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AdPlug.
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbinio-devel >= 1.4

%description devel
This is the package containing the header files for AdPlug library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki AdPlug.

%package static
Summary:	Static AdPlug library
Summary(pl.UTF-8):	Statyczna biblioteka AdPlug
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static AdPlug library.

%description static -l pl.UTF-8
Statyczna biblioteka AdPlug.

%prep
%setup -q
%patch0 -p1
%{__sed} -i 's@<string>@<string.h>@' src/player.h

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for system-wide adplugdb database
install -d $RPM_BUILD_ROOT/var/lib/adplug

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libadplug.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/adplugdb
%attr(755,root,root) %{_libdir}/libadplug-2.3.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libadplug-2.3.3.so.0
%{_mandir}/man1/adplugdb.1*
%dir /var/lib/adplug

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadplug.so
%{_includedir}/adplug
%{_pkgconfigdir}/adplug.pc
%{_infodir}/libadplug.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libadplug.a
