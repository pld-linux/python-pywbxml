Summary:	SynCE - Python bindings for libwbxml
Name:		synce-pywbxml
Version:	0.1
Release:	0.1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/synce/pywbxml-%{version}.tar.gz
# Source0-md5:	07f659f41d529d9b89da4a86db1e0ee8
URL:		http://www.synce.org/
BuildRequires:	libwbxml2-devel >= 0.9.2
BuildRequires:	python
BuildRequires:	python-Pyrex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

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
%{py_sitedir}/pywbxml.so
