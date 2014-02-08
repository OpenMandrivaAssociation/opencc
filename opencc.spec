%define major 1
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		opencc
Version:	0.2.0
Release:	7
Summary:	Simplified-Traditional Chinese Conversion
License:	ASL 2.0
Group:		System/Libraries
URL:		http://code.google.com/p/opencc
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

%package -n %{develname}
Summary:	Development tools for OpenCC
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
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
%{_datadir}/man/man1/*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdv2011.0
+ Revision: 666949
- mass rebuild

* Sat Jan 29 2011 Funda Wang <fwang@mandriva.org> 0.2.0-1
+ Revision: 633990
- new version 0.2.0

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.1.2-2mdv2011.0
+ Revision: 583522
- osbsoletes old package

* Fri Oct 01 2010 Funda Wang <fwang@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 582329
- update to new version 0.1.2

* Sat Aug 14 2010 Funda Wang <fwang@mandriva.org> 0.1.1-2mdv2011.0
+ Revision: 569521
- opensc is another package
- new version 0.1.1
- wrong devel name provided

* Sat Aug 14 2010 Funda Wang <fwang@mandriva.org> 0.1.0-5mdv2011.0
+ Revision: 569515
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.1.0-4mdv2011.0
+ Revision: 564187
- rebuild
- rebuild
- requires main package for data files
- import opencc


