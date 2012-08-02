%define target sh-elf
%define __spec_install_post\
    /usr/lib/rpm/brp-compress\
    /usr/lib/rpm/brp-strip
%define _binary_payload w7.xzdio

Name:           rockbox-%{target}-gcc
Version:        4.0.3
Release:        1%{?dist}
Summary:        Rockbox Cross Compiling GNU GCC targeted at %{target}
Group:          Development/Languages
License:        GPLv2+
URL:            http://gcc.gnu.org/
Source0:        ftp://ftp.gnu.org/gnu/gcc/gcc-%{version}/gcc-core-%{version}.tar.bz2
Source2:        README.fedora
Patch0:         http://www.rockbox.org/gcc/gcc-4.0.3-rockbox-1.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  rockbox-%{target}-binutils = 2.16.1, zlib-devel gawk
Requires:       rockbox-%{target}-binutils = 2.16.1

%description
This is a Cross Compiling version of GNU GCC, which can be used to
compile for the %{target} platform, instead of for the
native %{_arch} platform.

This package has been build for Rockbox development (http://www.rockbox.org).


%prep
%setup -q -c
pushd gcc-%{version}
%patch0 -p1

popd
cp -a %{SOURCE2} .

%build
mkdir -p gcc-%{target}
pushd gcc-%{target}
CC="%{__cc} ${RPM_OPT_FLAGS}" \
../gcc-%{version}/configure --prefix=%{_prefix} \
  --mandir=%{_mandir} --libdir=%{_libdir}  --infodir=%{_infodir} \
  --target=%{target} --enable-languages=c \
  --disable-nls --disable-libssp --with-system-zlib --disable-docs
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
* Sun Mar 11 2012 Dominik Riebeling <bluebrother@gmx.de> - 4.0.3-1
- initial version

