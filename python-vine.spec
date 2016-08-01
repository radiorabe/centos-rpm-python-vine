%global         srcname  vine

Name:           python-vine
Version:        1.1.1
Release:        1%{?dist}
Summary:        Promises, promises, promises
License:        BSD
URL:            https://pypi.python.org/pypi/vine
Source0:        https://pypi.python.org/packages/c9/d2/4fa0b92612efbf24f1614d6f27b4941795e7b577d5a6749f08c344f67c44/%{srcname}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  python-setuptools

BuildArch:      noarch

%{!?py2_build: %global py2_build CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build}
%{!?py2_install: %global py2_install %{__python} setup.py install --skip-build --root %{buildroot}}
%{!?python2_sitelib: %global python2_sitelib %{python_sitelib}}

%description
Promises, promises, promises

%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build

%install
%py2_install


%files
%{python2_sitelib}/%{srcname}
%{python2_sitelib}/%{srcname}-%{version}*.egg-info
