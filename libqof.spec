#%define api_version     1.0
#%define lib_major       8
#%define lib_name        %mklibname - %{api_version} %{lib_major}

Name: libqof
Version: 0.7.2
Release: %mkrel 1
Summary: QOF - Query Object Framework
License: GPL
Group: System/Libraries
Url: http://qof.sourceforge.net/
Source0: http://dl.sf.net/qof/qof-%version.tar.bz2
Patch0: %name-0.7.1.patch

BuildRequires: doxygen gcc-c++ graphviz libgda1.2-devel perl-XML-Parser sqlite-devel
BuildRequires: intltool libxml2-devel glib2-devel

%description
QOF - Query Object Framework is a library for adding a query engine
to C applications.  An SQL database is not needed; any collection
of C/C++ objects can act as 'tables' which can be 'joined' using
an SQL-like programming interface.

%package devel
Summary: Header files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contain header files for %name

%prep
%setup -q -n qof-%version
#%patch0 -p0
#
#autoconf

%build
%configure --disable-static
%make

%install
%makeinstall_std

rm -rf %{buildroot}/%{_datadir}/doc/libqof-devel/qof/.libs/

%find_lang qof

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f qof.lang
%doc README NEWS ChangeLog HACKING
%_libdir/*.so.*
%_datadir/xml/qof/

%files devel
#%{_docdir}/%{name}-devel/%{name}/*
%{_datadir}/doc/qof/html/doxy/*
#%{_datadir}/doc/%{name}-devel/qof/*
%_includedir/*
%_libdir/*.so
%{_libdir}/pkgconfig/qof-1.pc
#%{_libdir}/*.a
%{_libdir}/*.la
