Summary:	Color Font rendering library for X11R6
Summary(pl):	Biblioteki do renderowania fontСw pod X11R6
Name:		fnlib
Version:	0.5
Release:	6
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/Библиотеки
Group(uk):	X11/Б╕бл╕отеки
Source0:	ftp://www.rasterman.com/pub/enlightenment/libs/fnlib/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	imlib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
Fnlib is a library that provides full scalable 24-bit Color font
rendering abilities for X.

%description -l pl
Fnlib jest bibliotek╠, ktСra umo©liwia renderowanie fontСw
skalowalnych pod X11.

%package devel
Summary:	Fnlib headers and documentation
Summary(pl):	Pliki nagЁСwkowe oraz dokumentacja
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description -l pl devel
Pliki nagЁСwkowe oraz dokumentacja dla Fnliba.

%package static
Summary:	Fnlib static libraries 
Summary(pl):	Biblioteki statyczne fnlib
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Разработка/Библиотеки
Group(uk):	X11/Розробка/Б╕бл╕отеки
Requires:	%{name}-devel = %{version}

%description static
Fnlib static libraries.

%description -l pl static
Biblioteki statyczne fnlib.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
autoheader
automake -a -c
%configure

%{__make} fontsdir=%{_datadir}/fnlib_fonts

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf README doc/fontinfo.README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config %{_sysconfdir}/*
%{_datadir}/fnlib_fonts

%files devel
%defattr(644,root,root,755)
%doc doc/index.html doc/fontinfo.README.gz

%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
