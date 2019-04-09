Name: opencc
Version: 1.0.5
Release: %mkrel 3
Summary: Simplified-Traditional Chinese Conversion
License: ASL 2.0
Group: System/Internationalization
URL: https://github.com/BYVoid/OpenCC
Source0: https://github.com/BYVoid/OpenCC/archive/ver.%{version}/%{name}-%{version}.tar.gz
Patch0: opencc-fixes-cmake.patch
Patch1: opencc-1.0.3-ld_path.patch
Patch2: opencc-1.0.3-CVE-2018-16982.patch
BuildRequires: cmake

%description
OpenCC is an opensource project for conversion between Traditional Chinese and
Simplified Chinese, which supports phrase-level conversion and regional idioms
among Mainland China, Taiwan and Hong kong.

%define major 2
%define libname %mklibname opencc %major

%package -n %libname
Summary: Runtime library for OpenCC
Group: System/Libraries
Requires: %name

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
%setup -qn OpenCC-ver.%{version}
%autopatch -p1

%build
%cmake
%make_build

%install
%make_install -C build

%files
%doc AUTHORS
%{_bindir}/*
%{_datadir}/opencc

%files -n %{libname}
%{_libdir}/lib*.so.%{major}
%{_libdir}/lib*.so.1.0.0

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
