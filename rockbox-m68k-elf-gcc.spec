%define target m68k-elf
%define __spec_install_post\
    /usr/lib/rpm/brp-compress\
    /usr/lib/rpm/brp-strip
%define _binary_payload w7.xzdio

Name:           rockbox-%{target}-gcc
Version:        4.5.2
Release:        1%{?dist}
Summary:        Rockbox Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
License:        GPLv2+
URL:            http://gcc.gnu.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-core-%{version}.tar.bz2
Source2:        README.fedora

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  rockbox-%{target}-binutils = 2.20.1, zlib-devel gawk gmp-devel mpfr-devel libmpc-devel
Requires:       rockbox-%{target}-binutils = 2.20.1

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.

This package has been build for Rockbox development (http://www.rockbox.org).

%prep
%setup -q -c
cp -a %{SOURCE2} .

%build
mkdir -p gcc-%{target}
pushd gcc-%{target}

CC="%{__cc}" \
CFLAGS=-U_FORTIFY_SOURCE \
../gcc-%{version}/configure --prefix=%{_prefix} \
  --mandir=%{_mandir}  --infodir=%{_infodir} --libdir=%{_libdir} \
  --target=%{target} --enable-languages=c \
  --disable-nls --disable-libssp --with-system-zlib --disable-docs --with-arch=cf
# In general, building GCC is not smp-safe
make
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd gcc-%{target}
make install DESTDIR=$RPM_BUILD_ROOT
popd
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm -r $RPM_BUILD_ROOT%{_mandir}/man7
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a
# and these aren't usefull for embedded targets
rm -r $RPM_BUILD_ROOT%{_libdir}/gcc/%{target}/%{version}/install-tools
rm -r $RPM_BUILD_ROOT%{_libexecdir}/gcc/%{target}/%{version}/install-tools


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc gcc-%{version}/COPYING gcc-%{version}/COPYING.LIB
%doc gcc-%{version}/README README.fedora
%{_bindir}/%{target}-*
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/%{target}
%{_libdir}/gcc/%{target}/%{version}
%dir %{_libexecdir}/gcc
%dir %{_libexecdir}/gcc/%{target}
%{_libexecdir}/gcc/%{target}/%{version}
%{_mandir}/man1/%{target}-*.1.gz


%changelog
* Sun Mar 11 2012 Dominik Riebeling <bluebrother@gmx.de> - 4.5.2-1
- initial version

