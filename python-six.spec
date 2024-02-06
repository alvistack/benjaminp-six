# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-six
Version: 1.17.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python 2 and 3 compatibility utilities
License: MIT
URL: https://github.com/benjaminp/six/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500 || 0%{?rhel} == 7
%package -n python%{python3_version_nodots}-six
Summary: Python 2 and 3 compatibility utilities
Requires: python3
Provides: python3-six = %{version}-%{release}
Provides: python3dist(six) = %{version}-%{release}
Provides: python%{python3_version}-six = %{version}-%{release}
Provides: python%{python3_version}dist(six) = %{version}-%{release}
Provides: python%{python3_version_nodots}-six = %{version}-%{release}
Provides: python%{python3_version_nodots}dist(six) = %{version}-%{release}

%description -n python%{python3_version_nodots}-six
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions.

%files -n python%{python3_version_nodots}-six
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?rhel} == 7)
%package -n python3-six
Summary: Python 2 and 3 compatibility utilities
Requires: python3
Provides: python3-six = %{version}-%{release}
Provides: python3dist(six) = %{version}-%{release}
Provides: python%{python3_version}-six = %{version}-%{release}
Provides: python%{python3_version}dist(six) = %{version}-%{release}
Provides: python%{python3_version_nodots}-six = %{version}-%{release}
Provides: python%{python3_version_nodots}dist(six) = %{version}-%{release}

%description -n python3-six
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions.

%files -n python3-six
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
