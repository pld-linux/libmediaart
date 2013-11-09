#
# Conditional build:
%bcond_with	qt		# use Qt instead of GdkPixbuf for media extraction
%bcond_without	static_libs	# static library build
%bcond_without	vala		# Vala binding
#
Summary:	Media art extraction and cache management library
Summary(pl.UTF-8):	Biblioteka do wydobywania okładek i zarządzania ich pamięcią podręczną
Name:		libmediaart
Version:	0.1.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libmediaart/0.1/%{name}-%{version}.tar.xz
# Source0-md5:	c9b873f63ea621f2ae339163782b3f79
URL:		https://github.com/curlybeast/libmediaart
%{?with_qt:BuildRequires:	QtGui-devel >= 4.7.1}
%{!?with_qt:BuildRequires:	gdk-pixbuf2-devel >= 2.12.0}
BuildRequires:	glib2-devel >= 1:2.35.1
BuildRequires:	gobject-introspection-devel >= 1.30.0
BuildRequires:	gtk-doc >= 1.8
%{?with_qt:BuildRequires:	libstdc++-devel}
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	tar >= 1:1.22
BuildRequires:	tracker-devel >= 0.16.0
%{?with_vala:BuildRequires:	vala >= 2:0.16}
BuildRequires:	xz
BuildRequires:	zlib-devel
%{?with_qt:Requires:	QtGui >= 4.7.1}
%{!?with_qt:Requires:	gdk-pixbuf2 >= 2.12.0}
Requires:	glib2 >= 1:2.35.1
Requires:	tracker-libs >= 0.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Media art extraction and cache management library.

%description -l pl.UTF-8
Biblioteka do wydobywania okładek i zarządzania ich pamięcią
podręczną.

%package devel
Summary:	Header files for libmediaart library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmediaart
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_qt:Requires:	QtGui-devel >= 4.7.1}
%{!?with_qt:Requires:	gdk-pixbuf2-devel >= 2.12.0}
Requires:	glib2-devel >= 1:2.35.1
Requires:	tracker-devel >= 0.16.0
Requires:	zlib-devel

%description devel
Header files for libmediaart library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmediaart.

%package static
Summary:	Static libmediaart library
Summary(pl.UTF-8):	Statyczna biblioteka libmediaart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmediaart library.

%description static -l pl.UTF-8
Statyczna biblioteka libmediaart.

%package apidocs
Summary:	libmediaart API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki libmediaart
Group:		Documentation

%description apidocs
API documentation for libmediaart library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libmediaart.

%package -n vala-libmediaart
Summary:	Vala API for libmediaart library
Summary(pl.UTF-8):	API języka Vala dla biblioteki libmediaart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	vala >= 2:0.16

%description -n vala-libmediaart
Vala API for libmediaart library.

%description -n vala-libmediaart -l pl.UTF-8
API języka Vala dla biblioteki libmediaart.

%prep
%setup -q

%build
%configure \
	--enable-gdkpixbuf%{?with_qt:=no} \
	--disable-silent-rules \
	%{?with_static_libs:--enable-static} \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmediaart-0.2.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS
%attr(755,root,root) %{_libdir}/libmediaart-0.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmediaart-0.2.so.0
%{_libdir}/girepository-1.0/MediaArt-0.2.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmediaart-0.2.so
%{_includedir}/libmediaart-0.2
%{_datadir}/gir-1.0/MediaArt-0.2.gir
%{_pkgconfigdir}/libmediaart-0.2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libmediaart-0.2.a
%endif

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libmediaart

%if %{with vala}
%files -n vala-libmediaart
%defattr(644,root,root,755)
%{_datadir}/vala/vapi/libmediaart-0.2.vapi
%endif
