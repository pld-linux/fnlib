Summary:     Color Font rendering lobrary for X11R6
Summary(pl): Biblioteki do renderowania fontów pod X11R6
Name:        fnlib
Version:     0.3
Release:     2
Copyright:   LGPL
Group:       X11/Libraries
Source:      ftp://www.rasterman.com/pub/enlightenment/enlightenment/fnlib_DR-%{version}.tar.gz
Obsoletes:   Fnlib
URL:         http://www.rasterman.com/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Fnlib is a library that provides full scalable 24-bit Color font rendering
abilities for X.

%description -l pl
Fnlib jest bibliotek±, która umo¿liwia renderowanie fontów skalowalnych pod
X11.

%package devel
Summary:     Fnlib header files and development documentation
Summary(pl): Pliki nag³ówkowe oraz dokumentacja do Fnlib
Group:       X11/Libraries
Requires:    %{name} = %{version}
Obsoletes:   Fnlib

%description devel
Header files and documentation for Fnlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do Fnlib.

%package static
Summary:     Fnlib static libraries
Summary(pl): Bibliteki statyczne Fnlib
Group:       X11/Libraries
Requires:    %{name}-devel = %{version}

%description static
Fnlib static libraries.

%description static -l pl
Bibliteki statyczne Fnlib.

%prep
%setup -q -n fnlib

%build
./configure --prefix=/usr --sysconfdir=/etc
make CFLAGS=$RPM_OPT_FLAGS

%install
rm -rf $RPM_BUILD_ROOT
make install \
	prefix=$RPM_BUILD_ROOT/usr \
	sysconfdir=$RPM_BUILD_ROOT/etc

strip $RPM_BUILD_ROOT/usr/lib/lib*.so.*.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
/usr/lib/lib*.so.*.*
%config /etc/*
/usr/fnlib_fonts

%files devel
%defattr(644, root, root, 755)
%doc HACKING doc/{index.html,fontinfo.README}

/usr/lib/lib*.so
/usr/include/*
/usr/fnlib_fonts

%files static
%attr(644, root, root) /usr/lib/lib*.a

%changelog
* Thu Sep  3 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-2]
- added -q %setup parameter,
- adde pl translation (Wojtek ¦lusarczyk <wojtek@shadow.eu.org>),
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{version} macro in Source,
- added static subpackage
- removed Packager field,
- removed README from main package and doc/index.html and HACKING from
  devel,
- changeded dependences to "Requires: %%{name} = %%{version}" in devel
  subpackage.
- added full %attr description in %files,
- added striping shared libraries.
