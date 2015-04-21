Summary:	xlsfonts application - server font list displayer for X
Summary(pl.UTF-8):	Aplikacja xlsfonts - wyświetlanie listy fontów serwera X
Name:		xorg-app-xlsfonts
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xlsfonts-%{version}.tar.bz2
# Source0-md5:	6f5711bef8c765857a0887a91476283b
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1*
