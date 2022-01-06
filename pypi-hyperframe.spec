#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-hyperframe
Version  : 6.0.1
Release  : 16
URL      : https://files.pythonhosted.org/packages/5a/2a/4747bff0a17f7281abe73e955d60d80aae537a5d203f417fa1c2e7578ebb/hyperframe-6.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/5a/2a/4747bff0a17f7281abe73e955d60d80aae537a5d203f417fa1c2e7578ebb/hyperframe-6.0.1.tar.gz
Summary  : HTTP/2 framing layer for Python
Group    : Development/Tools
License  : MIT
Requires: pypi-hyperframe-license = %{version}-%{release}
Requires: pypi-hyperframe-python = %{version}-%{release}
Requires: pypi-hyperframe-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: hyperframe
Provides: hyperframe-python
Provides: hyperframe-python3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
======================================
hyperframe: Pure-Python HTTP/2 framing
======================================

%package license
Summary: license components for the pypi-hyperframe package.
Group: Default

%description license
license components for the pypi-hyperframe package.


%package python
Summary: python components for the pypi-hyperframe package.
Group: Default
Requires: pypi-hyperframe-python3 = %{version}-%{release}

%description python
python components for the pypi-hyperframe package.


%package python3
Summary: python3 components for the pypi-hyperframe package.
Group: Default
Requires: python3-core
Provides: pypi(hyperframe)

%description python3
python3 components for the pypi-hyperframe package.


%prep
%setup -q -n hyperframe-6.0.1
cd %{_builddir}/hyperframe-6.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641443540
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-hyperframe
cp %{_builddir}/hyperframe-6.0.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-hyperframe/931f71c3a491615b520ba37abf91e3c6bd6c6e46
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-hyperframe/931f71c3a491615b520ba37abf91e3c6bd6c6e46

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
