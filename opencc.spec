%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	Simplified-Traditional Chinese Conversion
Name:		opencc
Version:	0.2.0
Release:	6
License:	ASL 2.0
Group:		System/Libraries
Url:		http://code.google.com/p/opencc
Source0:	http://opencc.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		opencc-0.2.0-lib64.patch
Patch1:		opencc-0.2.0-static-lib.patch
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

%prep
%setup -q
%patch0 -p0 -b .lib64
%patch1 -p0 -b .static

%build
%cmake
%make

# Drop double slashes from .pc file, if any
sed -i 's#libdir=${prefix}/#libdir=${prefix}#' opencc.pc

%install
%makeinstall_std -C build

%files
%doc AUTHORS COPYING README
%{_bindir}/*
%{_datadir}/opencc
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libopencc.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

