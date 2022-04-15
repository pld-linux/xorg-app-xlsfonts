Summary:	xlsfonts application - server font list displayer for X
Summary(pl.UTF-8):	Aplikacja xlsfonts - wyświetlanie listy fontów serwera X
Name:		xorg-app-xlsfonts
Version:	1.0.7
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xlsfonts-%{version}.tar.xz
# Source0-md5:	f7397338c9cf1637492c8a4610b6cd0d
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xlsfonts lists the fonts that match the given pattern.

%description -l pl.UTF-8
xlsfonts wyświetla listę fontów pasujących do zadanego wzorca.

%prep
%setup -q -n xlsfonts-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*
