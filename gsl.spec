Summary:	The GNU Scientific Library for numerical analysis
Name:		gsl
Version:	1.16
Release:	1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnu.org/gnu/gsl/%{name}-%{version}.tar.gz
# Source0-md5:	e49a664db13d81c968415cd53f62bc8b
Patch0:		%{name}-link.patch
URL:		http://www.gnu.org/software/gsl/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The gsl package includes the GNU Scientific Library (GSL). The GSL is
a collection of routines for numerical analysis, written in C. The GSL
is in alpha development. It now includes a random number suite, an FFT
package, simulated annealing and root finding. In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

%package devel
Summary:	Header files for developing programs using gsl
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for developing programs using gsl.

%package progs
Summary:	gsl utility programs
Group:		Applications/Science
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description progs
gsl utility programs.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun devel
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost /%{_libdir}/libgsl.so.?
%attr(755,root,root) %ghost /%{_libdir}/libgslcblas.so.?
%attr(755,root,root) %{_libdir}/libgsl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgslcblas.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-config
%attr(755,root,root) %{_libdir}/libgsl.so
%attr(755,root,root) %{_libdir}/libgslcblas.so
%{_libdir}/libgsl.la
%{_libdir}/libgslcblas.la
%{_includedir}/gsl
%{_aclocaldir}/gsl.m4
%{_pkgconfigdir}/gsl.pc
%{_infodir}/gsl*.info*
%{_mandir}/man1/gsl-config.1*
%{_mandir}/man3/*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsl-histogram
%attr(755,root,root) %{_bindir}/gsl-randist
%{_mandir}/man1/gsl-histogram.1*
%{_mandir}/man1/gsl-randist.1*

