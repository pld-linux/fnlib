Summary:	Color Font rendering library for X11R6
Summary(pl):	Biblioteki do renderowania fontów pod X11R6
Name:		fnlib
Version:	0.4
Release:	11
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	XFree86-devel
BuildRequires:	imlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_sysconfdir	/etc/X11

%description
Fnlib is a library that provides full scalable 24-bit Color font rendering
abilities for X.

%description -l pl
Fnlib jest bibliotek±, która umo¿liwia renderowanie fontów skalowalnych pod
X11.

%package devel
Summary:	Fnlib headers and documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Headers and documentation for Fnlib.

%description -l pl devel
Pliki nag³ówkowe oraz dokumentacja dla Fnliba.

%package static
Summary:	Fnlib static libraries 
Summary(pl):	Biblioteki statyczne fnlib
Group:		X11/Development/Libraries
Group(pl):	X11/Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Fnlib static libraries.

%description -l pl static
Biblioteki statyczne fnlib.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make fontsdir=%{_datadir}/fnlib_fonts

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf {README,doc/fontinfo.README}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
%defattr(644,root,root)
%{_libdir}/lib*.a
