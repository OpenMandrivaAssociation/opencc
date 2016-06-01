%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}
%define static %mklibname -d -s %{name}
%define  _disable_lto 1

Summary:	Simplified-Traditional Chinese Conversion
Name:		opencc
Version:	1.0.4
Release:	1
License:	ASL 2.0
Group:		System/Libraries
Url:		http://code.google.com/p/opencc
Source0:	http://opencc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		opencc-fixes-cmake.patch
Patch1:		opencc-1.0.3-ld_path.patch
BuildRequires:	cmake

%description
OpenCC - Simplified-Traditional Chinese Conversion.

%package -n %{libname}
Summary:	Runtime library for OpenCC
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
Runtime Libraries for OpenCC.

%package -n %{devname}
Summary:	Development tools for OpenCC
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development tools for OpenCC.

%package -n	%{static}
Summary:	Development tools for OpenCC
Group:		Development/Other
Requires:	%{name}-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n %{devname}
Development tools for OpenCC.

%prep
%setup -q
%apply_patches

%build
%cmake
%make

# Drop double slashes from .pc file, if any
sed -i 's#libdir=${prefix}/#libdir=${prefix}#' opencc.pc

%install
%makeinstall_std -C build

%files
%doc AUTHORS
%{_bindir}/*
%{_datadir}/opencc
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libopencc.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n %{static}
%{_libdir}/*.a
