Name: opencc
Version: 0.1.2
Release: %mkrel 1
Summary: Simplified-Traditional Chinese Conversion
License: ASL 2.0
Group: System/Libraries
URL: http://code.google.com/p/open-chinese-convert/
Source0: http://open-chinese-convert.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
OpenCC - Simplified-Traditional Chinese Conversion.

%define libname %mklibname opencc 1
%package -n %libname
Summary: Runtime library for OpenCC
Group: System/Libraries
Requires: %name = %version-%release

%description -n %libname
Runtime Libraries for OpenCC.

%define develname %mklibname -d %{name}
%package -n %develname
Summary: Development tools for OpenCC
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
Development tools for OpenCC.

%prep
%setup -q

%build
%configure2_5x --disable-static --enable-shared
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/opencc
%{_datadir}/man/man1/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/lib*.so.1*

%files -n %{develname}
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
