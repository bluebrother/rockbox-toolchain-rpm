Rockbox toolchain RPM packages
==============================

Overview
--------

Rockbox_ is a replacement firmware for various digital music players.  For
building Rockbox known versions of the gcc compiler are used. Traditionally the
compiler is not distributed by Rockbox but only a script to build the toolchain
(see ``rockboxdev.sh`` at the CrossCompiler_ wiki page).

During DevConEuro2011_ it was agreed having distribution packages of the
compiler would be a good thing. This repository hold the ``spec`` files
required for building the compilers (arm-elf-eabi, m68k, sh1, mipsel) as
packages on Fedora. A helper script to setup the build tree (i.e. download the
gcc packages and custom Rockbox patches) is also included.

Building packages for other rpm based distributions might work but is not
tested.

Usage
-----
* setup your system to be able to build RPM packages.
* prepare the RPM buildroot by running ``rpmdev-setuptree`` (part of the
  ``rpmdevtools`` package)
* run ``prep.sh`` to download the required source packages from the internet
  and copy the ``spec`` files to the buildroot.
* build the binutils package(s)
* install the binutils package(s). This is necessary since building gcc
  requires binutils.
* build the gcc package(s).
* optionally build the ``rockbox-devel`` package. It will create multiple meta
  packages for pulling in the required dependencies and the cross compiler,
  assuming the built compilers are available in a yum repository.
  You might want to put a valid URL for the repository in the ``rockbox-repo``
  subpackage build receipe.
* install gcc package(s), or create a repository and install from it.

.. _Rockbox: http://www.rockbox.org
.. _DevConEuro2011: http://www.rockbox.org/wiki/DevConEuro2011
.. _CrossCompiler: http://www.rockbox.org/wiki/CrossCompiler
