%define devname %mklibname xsimd -d

Name: xsimd
Version: 12.1.1
Release: 1
Source0: https://github.com/xtensor-stack/xsimd/archive/%{version}/%{name}-%{version}.tar.gz
Summary: C++ wrappers for SIMD intrinsics and parallelized, optimized mathematical functions
License: BSD-3-Clause
Group: System/Libraries
BuildRequires: cmake
BuildRequires: ninja
BuildArch: noarch

%description
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that
has been available for many years. SIMD instructions perform a single operation
on a batch of values at once, and thus provide a way to significantly
accelerate code execution. However, these instructions differ between
microprocessor vendors and compilers.

xsimd provides a unified means for using these features for library authors.
Namely, it enables manipulation of batches of numbers with the same arithmetic
operators as for single values. It also provides accelerated implementation of
common mathematical functions operating on batches.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C

%description -n %{devname}
Development files (Headers etc.) for %{name}.

SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that
has been available for many years. SIMD instructions perform a single operation
on a batch of values at once, and thus provide a way to significantly
accelerate code execution. However, these instructions differ between
microprocessor vendors and compilers.

xsimd provides a unified means for using these features for library authors.
Namely, it enables manipulation of batches of numbers with the same arithmetic
operators as for single values. It also provides accelerated implementation of
common mathematical functions operating on batches.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{devname}
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
