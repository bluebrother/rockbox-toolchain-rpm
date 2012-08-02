Name:		rockbox
Version:	1
Release:	1%{?dist}
Summary:	Meta package to pull packages required for Rockbox development

Group:		Development/Tools
BuildArch:      noarch
License:	GPL
URL:		http://www.rockbox.org
%description
Rockbox development meta package

%package devel
Summary:        Rockbox development meta package
Requires:	gcc rockbox-arm-elf-eabi-gcc rockbox-m68k-elf-gcc rockbox-mipsel-elf-gcc rockbox-sh-elf-gcc perl python sed gawk make git patch zip curl SDL-devel
%description devel
This meta package pulls in all packages requried for Rockbox development.
Currently the following cross compilers are supported:
- sh-elf
- arm-elf-eabi
- m68k-elf
- mipsel-elf
- SDL (simulator builds)

%package manual
Summary:        Rockbox development manual meta package
Requires:       texlive-texmf-latex texlive-utils texlive-latex
%description manual
This meta package pulls in all packages required for building the Rockbox
manual. Building the manual requires to have a working Rockbox build setup
working.

%package repo
Summary:        Rockbox development yum repository
%description repo
Rockbox yum repository configuration.
%build
mkdir -p $RPM_BUILD_ROOT/etc/yum.repos.d
cat << EOF > $RPM_BUILD_ROOT/etc/yum.repos.d/rockbox.repo
[rockbox]
name=Rockbox
baseurl
enabled=1
gpgcheck=0
EOF

%install


%files devel
%files manual
%files repo
%defattr(-,root,root,-)
%{_sysconfdir}/yum.repos.d/rockbox.repo



%changelog
* Sat May 19 2012 Dominik Riebeling <bluebrother@gmx.de> - 1-1
- Initial version
