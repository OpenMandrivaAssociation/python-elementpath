%global module elementpath
%bcond tests 1

Name:		python-elementpath
Version:	5.1.3
Release:	1
Summary:	XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml
Group:		Development/Python
License:	MIT
URL:		https://github.com/sissaschool/elementpath
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(lxml)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif
# The doc build for this module requires the readthedocs-sphinx-search module
# that has been deprecated upstream since 2025/08/04 which we did not have
# packaged prior to its deprecation.
# Obsolete the old docs package to avoid adding a dependency on deprecated modules.
Obsoletes:	%{name}-doc < %{EVRD}

%description
XPath 1.0/2.0/3.0/3.1 parsers and selectors for ElementTree and lxml.

The proposal of this package is to provide XPath 1.0, 2.0, 3.0 and 3.1
selectors for ElementTree XML data structures, both for the standard
ElementTree library and for the lxml.etree library.

For lxml.etree this package can be useful for providing XPath 2.0/3.0/3.1
selectors, because lxml.etree already has it's own implementation of XPath 1.0.

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest
%endif

%files
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{module}
%{python3_sitelib}/%{module}-%{version}.dist-info
