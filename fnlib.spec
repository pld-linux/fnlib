Summary:	Color Font rendering library for X11R6
Summary(es):	Biblioteca de render de fuentes coloridas para el X11R6
Summary(pl):	Biblioteki do renderowania fontÛw pod X11R6
Summary(pt_BR):	Biblioteca para renderizaÁ„o colorida de fontes para o X11R6
Name:		fnlib
Version:	0.5
Release:	10
License:	LGPL
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(es):	X11/Bibliotecas
Group(fr):	X11/Librairies
Group(pl):	X11/Biblioteki
Group(pt_BR):	X11/Bibliotecas
Group(ru):	X11/‚…¬Ã…œ‘≈À…
Group(uk):	X11/‚¶¬Ã¶œ‘≈À…
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

%description -l es
Biblioteca de render de fuentes coloridas para el X11R6.

%description -l pl
Fnlib jest bibliotek±, ktÛra umoøliwia renderowanie fontÛw
skalowalnych pod X11.

%description -l pt_BR
A fnlib È uma biblioteca que fornece renderizaÁ„o completa e escal·vel
de 24 bits de cores para fontes no X.

%package devel
Summary:	Fnlib headers and documentation
Summary(es):	Archivos de inclusiÛn, bibliotecas est·ticas y documentaciÛn para fnlib
Summary(pl):	Pliki nag≥Ûwkowe oraz dokumentacja
Summary(pt_BR):	Arquivos de inclus„o, bibliotecas e documentaÁ„o para a fnlib
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description devel -l es
Archivos de inclusiÛn, bibliotecas est·ticas y documentaciÛn para
fnlib.

%description devel -l pl
Pliki nag≥Ûwkowe oraz dokumentacja dla Fnliba.

%description devel -l pt_BR
Arquivos de inclus„o, bibliotecas e documentaÁ„o para a fnlib.

%package static
Summary:	Fnlib static libraries 
Summary(es):	Static libraries for fnlib development
Summary(pl):	Biblioteki statyczne fnlib
Summary(pt_BR):	Bibliotecas est·ticas para desenvolvimento com fnlib
Group:		X11/Development/Libraries
Group(de):	X11/Entwicklung/Libraries
Group(es):	X11/Desarrollo/Bibliotecas
Group(fr):	X11/Development/Librairies
Group(pl):	X11/Programowanie/Biblioteki
Group(pt_BR):	X11/Desenvolvimento/Bibliotecas
Group(ru):	X11/Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	X11/Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Fnlib static libraries.

%description static -l es
Static libraries for fnlib development

%description static -l pl
Biblioteki statyczne fnlib.

%description static -l pt_BR
Bibliotecas est·ticas para desenvolvimento com fnlib

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
