Summary:	xlsfonts application - server font list displayer for X
Summary(pl.UTF-8):	Aplikacja xlsfonts - wyświetlanie listy fontów serwera X
Name:		xorg-app-xlsfonts
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xlsfonts-%{version}.tar.bz2
# Source0-md5:	28958248590ff60ecd70e8f590d977b7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xlsfonts
%{_mandir}/man1/xlsfonts.1x*
