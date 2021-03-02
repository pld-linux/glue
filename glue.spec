#
# Conditional build:
%bcond_with	python3	# use Python 3.x instead of 2.x
%bcond_with	tests	# unit tests (not present in 0.13 sources)

Summary:	A simple command line tool to generate CSS sprites
Summary(pl.UTF-8):	Proste narzędzie linii poleceń do generowania "duszków" CSS
Name:		glue
Version:	0.13
Release:	3
License:	BSD
Group:		Applications/Graphics
Source0:	http://files.pythonhosted.org/packages/source/g/glue/%{name}-%{version}.tar.gz
# Source0-md5:	65ac9f9b4667b7ef5f7665273b68bc56
Patch0:		%{name}-deps.patch
URL:		http://github.com/jorgebastida/glue
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-cssutils >= 0.9.10
BuildRequires:	python3-jinja2 >= 2.7
BuildRequires:	python3-pillow >= 2.2.2
%endif
%else
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-cssutils >= 0.9.10
BuildRequires:	python-jinja2 >= 2.7
BuildRequires:	python-mock >= 1.0
BuildRequires:	python-pillow >= 2.2.2
%endif
%endif
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python3}
Requires:	python3-jinja2 >= 2.7
Requires:	python3-modules >= 1:3.3
Requires:	python3-pillow >= 2.2.2
%else
Requires:	python-jinja2 >= 2.7
Requires:	python-modules >= 2.7
Requires:	python-pillow >= 2.2.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glue is a simple command line tool to generate CSS sprites using any
kind of source images like PNG, JPEG or GIF. Glue will generate a
unique PNG file containing every source image and a CSS file including
the necessary CSS classes to use the sprite.

%description -l pl.UTF-8
Glue to proste narzędzie linii poleceń do generowania "duszków"
(sprite'ów) CSS przy użyciu dowolnego rodzaju obrazów źródłowych (PNG,
JPEG, GIF). Glue generuje unikatowy plik PNG zawierający wszystkie
obrazy źródłowe oraz plik CSS zawierający klasy CSS potrzebne do
używania duszka.

%prep
%setup -q
%patch0 -p1

%{__rm} -r glue.egg-info

%build
%if %{with python3}
%py3_build %{?with_tests:test}
%else
%py_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%else
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README.rst docs
%attr(755,root,root) %{_bindir}/glue
%if %{with python3}
%{py3_sitescriptdir}/glue
%{py3_sitescriptdir}/glue-%{version}-py*.egg-info
%else
%{py_sitescriptdir}/glue
%{py_sitescriptdir}/glue-%{version}-py*.egg-info
%endif
