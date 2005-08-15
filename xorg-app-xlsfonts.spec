# $Rev: 3403 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	xlsfonts application
Summary(pl):	Aplikacja xlsfonts
Name:		xorg-app-xlsfonts
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xlsfonts-%{version}.tar.bz2
# Source0-md5:	4e4b1e0088e4144e5ee1f1e1ab8a544b
Patch0:		xlsfonts-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/xlsfonts-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xlsfonts application.

%description -l pl
Aplikacja xlsfonts.


%prep
%setup -q -n xlsfonts-%{version}
%patch0 -p1


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
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*