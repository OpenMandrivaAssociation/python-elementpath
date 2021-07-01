# Created by pyp2rpm-3.3.5
%global pypi_name elementpath
%bcond_with bootstrap

Name:           python-%{pypi_name}
Version:        2.1.1
Release:        1
Summary:        XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Group:          Development/Python
License:        MIT
URL:            https://github.com/sissaschool/elementpath
Source0:        %{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
*********** elementpath *********** :target:
%package -n python-%{pypi_name}-doc
Summary:        elementpath documentation
%description -n python-%{pypi_name}-doc
Documentation for elementpath

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%if %{with bootstrap}
%check
%{__python3} setup.py test
%endif

%files -n python-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE
