%define major 1.1
%define oldlibname %mklibname opencc 2
%define libname %mklibname opencc
%define develname %mklibname -d %{name}

Name:		opencc
Version:	1.1.9
Release:	1
Summary:	Simplified-Traditional Chinese Conversion
License:	ASL 2.0
Group:		System/Internationalization
URL:		https://github.com/BYVoid/OpenCC
Source0:	https://github.com/BYVoid/OpenCC/archive/ver.%{version}/OpenCC-ver.%{version}.tar.gz
Patch1:		opencc-1.0.3-ld_path.patch
BuildSystem:	cmake
BuildRequires:	python%{pyver}dist(pybind11)
BuildRequires:	pkgconfig(RapidJSON)
BuildOption:	-DUSE_SYSTEM_PYBIND11:BOOL=ON
BuildOption:	-DUSE_SYSTEM_RAPIDJSON:BOOL=ON

%description
OpenCC is an opensource project for conversion between Traditional Chinese and
Simplified Chinese, which supports phrase-level conversion and regional idioms
among Mainland China, Taiwan and Hong kong.

%package -n %{libname}
Summary:	Runtime library for OpenCC
Group:		System/Libraries
Requires:	%{name}
%rename %{oldlibname}

%description -n %{libname}
Runtime Libraries for OpenCC.

%package -n %{develname}
Summary:	Development tools for OpenCC
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development tools for OpenCC.

%files
%doc AUTHORS
%{_bindir}/*
%{_datadir}/opencc

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/opencc
%{_libdir}/libmarisa.a
