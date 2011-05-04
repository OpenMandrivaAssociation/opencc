Name: opencc
Version: 0.2.0
Release: %mkrel 2
Summary: Simplified-Traditional Chinese Conversion
License: ASL 2.0
Group: System/Libraries
URL: http://code.google.com/p/opencc
Source0: http://opencc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0: opencc-0.2.0-lib64.patch
Patch1: opencc-0.2.0-static-lib.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: cmake

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
Obsoletes: %{_lib}opensc-devel

%description -n %develname
Development tools for OpenCC.

%prep
%setup -q
%patch0 -p0 -b .lib64
%patch1 -p0 -b .static

%build
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

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
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
