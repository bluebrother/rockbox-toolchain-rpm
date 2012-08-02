%define target mipsel-elf
%define __spec_install_post\
    /usr/lib/rpm/brp-compress\
    /usr/lib/rpm/brp-strip
%define _binary_payload w7.xzdio

Name:           rockbox-%{target}-binutils
Version:        2.17
Release:        1%{?dist}
Summary:        Rockbox Cross Compiling GNU binutils targeted at %{target}
Group:          Development/Tools
License:        GPLv2+
URL:            http://www.gnu.org/software/binutils/
Source0:        ftp://ftp.gnu.org/pub/gnu/binutils/binutils-%{version}.tar.bz2
Source1:        README.fedora
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildRequires:  gawk texinfo

%description
This is a Cross Compiling version of GNU binutils, which can be used to
assemble and link binaries for the %{target} platform, instead of for the
native %{_arch} platform.

This package has been build for Rockbox development (http://www.rockbox.org).


%prep
%setup -q -c

cp %{SOURCE1} .


%build
mkdir -p build
pushd build
CFLAGS="$RPM_OPT_FLAGS -U_FORTIFY_SOURCE" ../binutils-%{version}/configure \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
  --target=%{target} --disable-werror --disable-nls --disable-docs
make %{?_smp_mflags}
popd build


%install
rm -rf $RPM_BUILD_ROOT
pushd build
make install DESTDIR=$RPM_BUILD_ROOT
popd build
# these are for win targets only
rm $RPM_BUILD_ROOT%{_mandir}/man1/%{target}-{dlltool,nlmconv,windres}.1
# we don't want these as we are a cross version
rm -r $RPM_BUILD_ROOT%{_infodir}
rm    $RPM_BUILD_ROOT%{_libdir}/libiberty.a


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc binutils-%{version}/COPYING binutils-%{version}/COPYING.LIB
%doc binutils-%{version}/README README.fedora
%{_prefix}/%{target}
%{_bindir}/%{target}-*
%{_mandir}/man1/%{target}-*.1.gz


%changelog
* Sun Mar 11 2012 Dominik Riebeling <bluebrother@gmx.de> - 2.17-1
- initial version

