Name:           fnott
Version:        1.4.1
Release:        1
Summary:        Lightweight notification daemon for Wayland
License:        MIT
Group:          System/GUI/Wayland
URL:            https://codeberg.org/dnkl/fnott
Source0:        https://codeberg.org/dnkl/fnott/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  meson >= 0.58
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  scdoc
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fcft) < 4.0.0
BuildRequires:  pkgconfig(fcft) >= 3.0.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(tllist) >= 1.0.1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

%description
Lightweight notification daemon for Wayland.

%prep
%autosetup -p1 -n %{name}

%package        zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Requires:       zsh
BuildArch:      noarch

%description    zsh-completion
Zsh command-line completion support for %{name}

%build
%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/fnott
%{_bindir}/fnottctl

#{_mandir}/man1/fnott.1%{?ext_man}
#{_mandir}/man1/fnottctl.1%{?ext_man}
#{_mandir}/man5/fnott.ini.5%{?ext_man}

%dir %{_datadir}/doc/%{name}
%license %{_datadir}/doc/%{name}/LICENSE
%doc %{_datadir}/doc/%{name}/README.md
%doc CHANGELOG.md

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/fnott.ini
%{_datadir}/applications/fnott.desktop

%files zsh-completion
%{_datadir}/zsh/site-functions/_fnott
%{_datadir}/zsh/site-functions/_fnottctl
