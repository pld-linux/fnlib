Summary:	Color Font rendering library for X11R6
Summary(es):	Biblioteca de render de fuentes coloridas para el X11R6
Summary(pl):	Biblioteki do renderowania fontów pod X11R6
Summary(pt_BR):	Biblioteca para renderização colorida de fontes para o X11R6
Name:		fnlib
Version:	0.5
Release:	10
License:	LGPL
Group:		X11/Libraries
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	42093ed5b684da01e7a674b2adac52c7
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/X11

%description
Fnlib is a library that provides full scalable 24-bit Color font
rendering abilities for X.

%description -l es
Biblioteca de render de fuentes coloridas para el X11R6.

%description -l pl
Fnlib jest bibliotek±, która umo¿liwia renderowanie fontów
skalowalnych pod X11.

%description -l pt_BR
A fnlib é uma biblioteca que fornece renderização completa e escalável
de 24 bits de cores para fontes no X.

%package devel
Summary:	Fnlib headers and documentation
Summary(es):	Archivos de inclusión, bibliotecas estáticas y documentación para fnlib
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja
Summary(pt_BR):	Arquivos de inclusão, bibliotecas e documentação para a fnlib
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description devel -l es
Archivos de inclusión, bibliotecas estáticas y documentación para
fnlib.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja dla Fnliba.

%description devel -l pt_BR
Arquivos de inclusão, bibliotecas e documentação para a fnlib.

%package static
Summary:	Fnlib static libraries
Summary(pl):	Biblioteki statyczne fnlib
Summary(pt_BR):	Bibliotecas estáticas para desenvolvimento com fnlib
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Fnlib static libraries.

%description static -l pl
Biblioteki statyczne fnlib.

%description static -l pt_BR
Bibliotecas estáticas para desenvolvimento com fnlib

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} fontsdir=%{_datadir}/fnlib_fonts

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%config %{_sysconfdir}/*
%{_datadir}/fnlib_fonts

%files devel
%defattr(644,root,root,755)
%doc doc/index.html doc/fontinfo.README

%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
