# TODO: rename to either synce-pywbxml.spec or python-pywbxml.spec
Summary:	SynCE - Python bindings for wbxml2
Summary(pl.UTF-8):	SynCE - wiązania Pythona do biblioteki wbxml2
Name:		synce-pywbxml
Version:	0.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/pywbxml-%{version}.tar.gz
# Source0-md5:	6a1181b7be09ba69fe6768a0f6156416
URL:		http://www.synce.org/
BuildRequires:	libwbxml2-devel >= 0.9.2
BuildRequires:	pkgconfig
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE - Python bindings for wbxml2.

%description -l pl.UTF-8
SynCE - wiązania Pythona do biblioteki wbxml2.

%prep
%setup -q -n pywbxml-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/pywbxml.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING
%attr(755,root,root) %{py_sitedir}/pywbxml.so
