Summary:	AdLib sound player library
Summary(pl):	Biblioteka odtwarzacza d¼wiêku AdLib
Name:		adplug
Version:	2.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
# Source0-md5:	48c1bb7c8618c45596d79767dec2e962
Patch0:		%{name}-info.patch
URL:		http://adplug.sourceforge.net/
BuildRequires:	libbinio-devel >= 1.4
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	texinfo
Requires:	libbinio >= 1.4
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
Requires:	libbinio-devel >= 1.4

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
%patch0 -p1

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# for system-wide adplugdb database
install -d $RPM_BUILD_ROOT/var/lib/adplug

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/adplugdb
%attr(755,root,root) %{_libdir}/libadplug-*.so.*.*.*
%{_mandir}/man1/adplugdb.1*
%dir /var/lib/adplug

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libadplug.so
%{_libdir}/libadplug.la
%{_includedir}/%{name}
%{_pkgconfigdir}/adplug.pc
%{_infodir}/libadplug.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libadplug.a
