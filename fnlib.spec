Summary:	Color Font rendering lobrary for X11R6
Summary(pl):	Biblioteki do renderowania fontów pod X11R6
Name:		fnlib
Version:	0.4
Release:	1d
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}-%{version}.tar.gz
Requires:	imlib >= 1.9.2
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Fnlib is a library that provides full scalable 24-bit Color font rendering
abilities for X.

%description -l pl
Fnlib jest bibliotek±, która umo¿liwia renderowanie fontów skalowalnych pod
X11.

%package	devel
Summary:	Fnlib headers and documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja dla Fnliba.

%package static
Summary:	Fnlib static libraries 
Summary(pl):	Biblioteki statyczne fnlib
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Fnlib static libraries 

%description -l pl static
Biblioteki statyczne fnlib

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--sysconfdir=/etc/X11
make fontsdir=/usr/X11R6/share/fnlib_fonts

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

chmod 755 $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*
strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

bzip2 -9 doc/fontinfo.README README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.bz2

%attr(755,root,root) /usr/X11R6/lib/lib*.so.*
%config /etc/X11/*
/usr/X11R6/share/fnlib_fonts

%files devel
%defattr(644,root,root,755)
%doc doc/index.html doc/fontinfo.README.bz2

%attr((755,root,root) /usr/X11R6/lib/lib*.so
/usr/X11R6/include/*

%files static
%defattr(644,root,root,755)
/usr/X11R6/lib/*.a

%changelog
* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.4-1]
- changed base Source Url to ftp://ftp.gnome.org/pub/GNOME/sources/,
- sysconfdir changed to /etc/X11,
- removed HACKING from %doc,
- added useing DESTDIR in "make install",
- added LDFLAGS="-s" to ./configure enviroment.

* Mon Oct 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-4]
- header files moved to /usr/X11R6/include,
- fontsdir changed to /usr/X11R6/share/fnlib_fonts.

* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.3-3]
- added pl translation.

* Tue Jul 07 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.3-2]
- start at Raster spec,
- added %changelog,
- build against GNU libc-2.1.
