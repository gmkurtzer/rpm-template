Name: template-specfile
Version: 0.1
Release: 1.foo
Summary: This is an example specfile
License: GMK License v0.1
URL: http://www.template-specfile.org
Source0: template-release
Source1: testfile
BuildRequires: bash
Requires: bash


%description
This is a long description about the package and what the template-specfile
is all about. It will go to the next line prefixed with a "%"


%prep
# Prep scriptlet

# This is the setup macro for splatting out sources and preparing build environment
# %setup


%build
# Build scriptlet

# This is the configure macro for GNU style ./configure scripts (replace the hash with a '%')
#configure


%install
# Install scriptlet
# note: make sure all files are installed to the $RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT
# make install DESTDIR=$RPM_BUILD_ROOT

# for example:
mkdir -p $RPM_BUILD_ROOT/etc/template
install -m 644 %SOURCE0 $RPM_BUILD_ROOT/etc/template-release
install -m 644 %SOURCE1 $RPM_BUILD_ROOT/etc/template/testfile

%clean
# Clean scriptlet
rm -rf $RPM_BUILD_ROOT

%files
# File section
# note: include ALL files in the $RPM_BUILD_ROOT and omit the build directorty path
%defattr(-,root,root,-)
%dir /etc/template
/etc/template/*
/etc/template-release


%changelog
# Changelog section
* Fri Oct 06 2023 Gregory Kurtzer <gmkurtzer@gmail.com> 
- Example specfile updated
* Fri Oct 06 2023 Gregory Kurtzer <gmkurtzer@gmail.com> 
- Example specfile created
