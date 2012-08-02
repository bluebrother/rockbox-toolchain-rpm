#!/bin/bash

#
# - install rpmdevtools
# - prepare buildroot by running "rpmdev-setuptree"

RPMSRCDIR=$(rpm --eval "%{_sourcedir}")
RPMSPECDIR=$(rpm --eval "%{_specdir}")

SPECS=$(ls *.spec)

DLSOURCES="binutils/binutils-2.16.1.tar.bz2
    binutils/binutils-2.17.tar.bz2
    binutils/binutils-2.20.1.tar.bz2
    gcc/gcc-core-4.0.3.tar.bz2
    gcc/gcc-core-4.1.2.tar.bz2
    gcc/gcc-core-4.4.4.tar.bz2
    gcc/gcc-core-4.5.2.tar.bz2"
DLSOURCEURL=http://www.nic.funet.fi/pub/gnu/ftp.gnu.org/pub/gnu
DLPATCHES="binutils-2.20.1-ld-thumb-interwork-long-call.diff
    rockbox-multilibs-arm-elf-gcc-4.0.3_3.diff
    rockbox-multilibs-noexceptions-arm-elf-eabi-gcc-4.4.2_1.diff
    gcc-4.0.3-rockbox-1.diff"
DLPATCHURL=http://www.rockbox.org/gcc

for s in $DLSOURCES; do
    WHAT=$DLSOURCEURL/$s
    WHERE=$RPMSRCDIR/$(basename $s)
    if [ ! -f $WHERE ]; then
        echo "Downloading $WHAT"
        echo "  to $WHERE"
        curl -o $WHERE $WHAT
    fi
done

for s in $DLPATCHES; do
    WHAT=$DLPATCHURL/$s
    WHERE=$RPMSRCDIR/$(basename $s)
    if [ ! -f $WHERE ]; then
        echo "Downloading $WHAT"
        echo "  to $WHERE"
        curl -o $WHERE $WHAT
    fi
done

cp $SPECS $RPMSPECDIR
cp README.fedora $RPMSRCDIR

echo "Finished preparing your RPM build tree."
echo "Now change to $RPMSPECDIR and run"
echo "  rpmbuild -ba rockbox-*-binutils.spec"
echo "Then install the created packages and continue to build gcc"
echo "  rpmbuild -ba rockbox-*-gcc.spec"
echo
echo "Building the remaining rockbox-devel is not necessary. It is a meta"
echo "package to pull in all required depenencies. It is useful if you want to"
echo "setup a yum repository."

