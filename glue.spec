Summary:	A simple command line tool to generate CSS sprites
Name:		glue
Version:	0.9.1
Release:	1
License:	BSD
Group:		Applications/Graphics
Source0:	http://pypi.python.org/packages/source/g/glue/%{name}-%{version}.tar.gz
# Source0-md5:	6f431c294f4efa20921af82f4125645b
URL:		http://github.com/jorgebastida/glue
BuildRequires:	python-cssutils
BuildRequires:	python-devel
BuildRequires:	python-mock
BuildRequires:	python-setuptools
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-jinja2
Requires:	python-pillow
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Glue is a simple command line tool to generate CSS sprites using any
kind of source images like PNG, JPEG or GIF. Glue will generate a
unique PNG file containing every source image and a CSS file including
the necessary CSS classes to use the sprite.

%prep
%setup -q
rm -r glue.egg-info

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING docs
%attr(755,root,root) %{_bindir}/glue
%dir %{py_sitescriptdir}/glue
%{py_sitescriptdir}/glue/*.py[co]
%{py_sitescriptdir}/glue/algorithms
%{py_sitescriptdir}/glue/formats
%{py_sitescriptdir}/glue/managers
%{py_sitescriptdir}/glue-%{version}-py*.egg-info
