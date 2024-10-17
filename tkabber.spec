%define svnrev svn1948

Summary:	Client for the Jabber instant messaging system
Name:		tkabber
Version:	0.11.1
Release:	0.%{svnrev}.1
License:	GPLv2+
Group:		Networking/Instant messaging
Url:		https://tkabber.jabber.ru/
Source0:	%{name}-%{version}.tar.bz2
# for relase version:
#Source0:	http://files.jabber.ru/tkabber/%{name}-%{version}.tar.gz
# script to get tkabber from svn
Source1:	tkabber-snapshot.sh
Source2:	tkabber.png
Source3:	tkabber.desktop
Source4:	tkabber
Source5:	tkabber-remote
Patch0:		tkabber-0.11.1-install.patch
BuildRequires:	desktop-file-utils
# Only to make sure we have these in repositories:
BuildRequires:	tcl-tcllib
BuildRequires:	bwidget
BuildRequires:	tcltls
BuildRequires:	tkimg
BuildRequires:	tdom
BuildRequires:	tktray
BuildRequires:	tcl-tclxml
BuildRequires:	tcl-tkpng
BuildRequires:	tcl-zlib
Requires:	tcl-tcllib
Requires:	bwidget
Requires:	tcltls
Requires:	tkimg
Requires:	tdom
Requires:	tktray
Requires:	tcl-tclxml
Requires:	tcl-tkpng
Requires:	tcl-zlib
BuildArch:	noarch

%description
Tkabber is a Free and Open Source client for the Jabber
instant messaging system. It's written in Tcl/Tk, and
works on many platforms. The choice of Tcl/Tk for a Jabber
client is three-fold:
* it is portable: once you install a Tcl/Tk interpreter on
  your system, the Tkabber script "just runs" — without having
  to compile anything;
* it is customizable: Tkabber reads a configuration file when
  it starts that tells it the settings of various parameters; and,
* it is extensible: the configuration file is actually a Tcl
  script, so you can replace or augment entire portions of Tkabber
  (if you're so inclined).

%files
%doc AUTHORS COPYING ChangeLog README doc/tkabber.html
%{_bindir}/tkabber
%{_bindir}/tkabber-remote
%{_datadir}/tkabber
%{_datadir}/applications/tkabber.desktop
%{_datadir}/pixmaps/tkabber.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .install

%build
# nothing

%install
make install-bin DESTDIR=%{buildroot}

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}

mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_bindir}

install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/tkabber.png
install -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/tkabber
install -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/tkabber-remote

