Name: bc
Version: 1.07.1
Release: 1.gmk
Summary: This is an example specfile for CPIO
License: GPLv2+
URL: https://www.gnu.org/software/bc/
Source0: https://ftp.gnu.org/gnu/bc/bc-%{version}.tar.gz
BuildRequires: gcc
BuildRequires: make
BuildRequires: readline-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: texinfo
BuildRequires: ed

%description
bc is an arbitrary precision numeric processing language. Syntax is similar to
C, but differs in many substantial areas. It supports interactive execution of
statements. bc is a utility included in the POSIX P1003.2/D11 draft standard.

Since the POSIX document does not specify how bc must be implemented, this
version does not use the historical method of having bc be a compiler for the
dc calculator. This version has a single executable that both compiles the
language and runs the resulting “byte code“. The byte code is not the dc
language.


%prep
# Prep scriptlet

# This is the setup macro for splatting out sources and preparing build environment
# and patching (if any)
%autosetup


%build
# Build scriptlet

# This is the configure macro for running GNU style ./configure scripts with
# preconfigured options
%configure --with-readline

# Make helper macro
%make_build


%install
# Install scriptlet
# note: make sure all files are installed to the $RPM_BUILD_ROOT

# Make install helper macro
%make_install
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir


%clean
# Clean scriptlet
rm -rf $RPM_BUILD_ROOT

%files
# File section
# note: include ALL files in the $RPM_BUILD_ROOT and omit the build directorty path
%defattr(-,root,root,-)
%license COPYING COPYING.LIB
%doc FAQ AUTHORS NEWS README Examples/
%{_bindir}/dc
%{_bindir}/bc
%{_mandir}/*/*
%{_infodir}/*



%changelog
# Changelog section
* Fri Oct 06 2023 Gregory Kurtzer <gmkurtzer@gmail.com> 
- Example specfile updated
* Fri Oct 06 2023 Gregory Kurtzer <gmkurtzer@gmail.com> 
- Example specfile created
