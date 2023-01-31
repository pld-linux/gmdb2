Summary:	gmdb2 - graphical interface for MDB Tools
Summary(pl.UTF-8):	gmdb2 - graficzny interfejs do narzędzi MDB
Name:		gmdb2
Version:	0.9.1
Release:	1
License:	GPL v2+
Group:		Applications/Databases
#Source0Download: https://github.com/mdbtools/gmdb2/releases
Source0:	https://github.com/mdbtools/gmdb2/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	7fd322ded728c476ccc2a69998ba339c
Source1:	gmdb2.desktop
Source2:	gmdb2.png
URL:		https://github.com/mdbtools/gmdb2
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gtk+3-devel >= 3.22
BuildRequires:	mdbtools-devel >= 0.9.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	yelp-tools
Requires:	glib2 >= 1:2.26
Obsoletes:	mdbtools-gui < 0.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the official GUI for mdbtools. This standalone package (which
was included with mdbtools prior to version 0.9.0) is considered
beta-quality software.

%description -l pl.UTF-8
Ten program to oficjalne GUI do mdbtools. Ten samodzielny pakiet
(dołączany do mdbtools przed wersją 0.9.0) jest uznawany za
oprogramowanie o jakości beta.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless currently (any plugins?)
%{__rm} $RPM_BUILD_ROOT%{_includedir}/gmdb.h

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/gmdb2.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/gmdb2.png

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG.md README.md TODO
%attr(755,root,root) %{_bindir}/gmdb2
%{_datadir}/glib-2.0/schemas/mdbtools.gmdb2.gschema.xml
%{_datadir}/gmdb
%{_desktopdir}/gmdb2.desktop
%{_pixmapsdir}/gmdb2.png
%{_mandir}/man1/gmdb2.1*
