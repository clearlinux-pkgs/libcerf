#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
Name     : libcerf
Version  : 1.17
Release  : 15
URL      : https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v1.17/libcerf-v1.17.tar.gz
Source0  : https://jugit.fz-juelich.de/mlz/libcerf/-/archive/v1.17/libcerf-v1.17.tar.gz
Summary  : Complex error function library
Group    : Development/Tools
License  : MIT
Requires: libcerf-lib = %{version}-%{release}
Requires: libcerf-license = %{version}-%{release}
BuildRequires : buildreq-cmake
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Files:
- a LICENSE statement
- use_libcerf_mod.f90 : the f95 interface to cerflib
- cerflib_main_test.f90 : a main program exemplifying the calls to the cerflib functions
from Fortran95

Prerequisites:
- a modern f95 compiler including a f2003-standard ISO_C_BINDING module,
like e.g. gfortran (4.6 or better) or ifort
- libcerf installed and in the path where the linker searches for libraries
(if this is not so, you have to give the path in the command line when compiling,
preceded by -L, as usual)

%package dev
Summary: dev components for the libcerf package.
Group: Development
Requires: libcerf-lib = %{version}-%{release}
Provides: libcerf-devel = %{version}-%{release}
Requires: libcerf = %{version}-%{release}

%description dev
dev components for the libcerf package.


%package doc
Summary: doc components for the libcerf package.
Group: Documentation

%description doc
doc components for the libcerf package.


%package lib
Summary: lib components for the libcerf package.
Group: Libraries
Requires: libcerf-license = %{version}-%{release}

%description lib
lib components for the libcerf package.


%package license
Summary: license components for the libcerf package.
Group: Default

%description license
license components for the libcerf package.


%prep
%setup -q -n libcerf-v1.17
cd %{_builddir}/libcerf-v1.17

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685636547
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v4 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86_64-v4 -mprefer-vector-width=512 "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1685636547
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcerf
cp %{_builddir}/libcerf-v%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libcerf/a60a8d7195921cdf4dd97d3b150a2cc50ac115da || :
cp %{_builddir}/libcerf-v%{version}/fortran/ccerflib_f95_interface/LICENSE %{buildroot}/usr/share/package-licenses/libcerf/c5e64621385e175c53415e3c48d4627775c4ee8e || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/cerf.h
/usr/lib64/libcerf.so
/usr/lib64/pkgconfig/libcerf.pc
/usr/share/man/man3/cdawson.3
/usr/share/man/man3/cerf.3
/usr/share/man/man3/cerfc.3
/usr/share/man/man3/cerfcx.3
/usr/share/man/man3/cerfi.3
/usr/share/man/man3/dawson.3
/usr/share/man/man3/erfcx.3
/usr/share/man/man3/erfi.3
/usr/share/man/man3/im_w_of_z.3
/usr/share/man/man3/voigt.3
/usr/share/man/man3/voigt_hwhm.3
/usr/share/man/man3/w_of_z.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/cerf/html/cdawson.html
/usr/share/doc/cerf/html/cerf.html
/usr/share/doc/cerf/html/cerfc.html
/usr/share/doc/cerf/html/cerfcx.html
/usr/share/doc/cerf/html/cerfi.html
/usr/share/doc/cerf/html/dawson.html
/usr/share/doc/cerf/html/erfcx.html
/usr/share/doc/cerf/html/erfi.html
/usr/share/doc/cerf/html/im_w_of_z.html
/usr/share/doc/cerf/html/voigt.html
/usr/share/doc/cerf/html/voigt_hwhm.html
/usr/share/doc/cerf/html/w_of_z.html

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libcerf.so.1.17
/V4/usr/lib64/libcerf.so.1.17
/usr/lib64/libcerf.so.1
/usr/lib64/libcerf.so.1.17

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcerf/a60a8d7195921cdf4dd97d3b150a2cc50ac115da
/usr/share/package-licenses/libcerf/c5e64621385e175c53415e3c48d4627775c4ee8e
