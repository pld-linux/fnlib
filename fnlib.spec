Summary:     Color Font rendering lobrary for X11R6
Summary(pl): Biblioteki do renderowania fontów pod X11R6
Name:        fnlib
Version:     0.3
Release:     3
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://www.rasterman.com/pub/enlightenment/libs/fnlib/%{name}_DR-%{version}.tar.gz
Requires:    imlib >= 1.8.1
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Fnlib is a library that provides full scalable 24-bit Color font rendering
abilities for X.

%description -l pl
Fnlib jest bibliotek±, która umo¿liwia renderowanie fontów skalowalnych pod X11. 

%package devel
Summary:     Fnlib headers and documentation
Summary(pl): Pliki nag³ówkowe oraz dokumentacja
Group:       X11/Libraries
Requires:    %{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja dla Fnliba.

%package static
Summary:     Fnlib static libraries 
Summary(pl): Biblioteki statyczne fnlib
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Fnlib static libraries 

%description -l pl static
Biblioteki statyczne fnlib

%prep
%setup -q -n %{name}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6 \
	--includedir=/usr/X11R6/include/X11 \
	--sysconfdir=/etc
make 

%install
rm -rf $RPM_BUILD_ROOT
make install \
    prefix=$RPM_BUILD_ROOT/usr/X11R6 \
    includedir=$RPM_BUILD_ROOT/usr/X11R6/include/X11 \
    sysconfdir=$RPM_BUILD_ROOT/etc

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644, root, root, 755)
%doc README
%attr(755, root, root) /usr/X11R6/lib/lib*.so.*.*
%config /etc/*
/usr/X11R6/fnlib_fonts

%files devel
%defattr(644, root, root, 755)
%doc HACKING doc/index.html doc/fontinfo.README
/usr/X11R6/lib/lib*.so
/usr/X11R6/include/X11/*

%files static
%attr(644, root,root) /usr/X11R6/lib/*.a

%changelog
* Sat Sep 26 1998 Arkadiusz Mi¶kiewicz <misiek@misiek.eu.org>
  [0.3-3]
- added polish translation.

* Tue Jul 07 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.3-2]
- start at Raster spec,
- added %changelog.
