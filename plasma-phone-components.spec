%define snapshot 20200824

Name:		plasma-phone-components
Version:	0.0
Release:	0.%{snapshot}.1
Summary:	Plasma components for mobile phones
# https://invent.kde.org/plasma/plasma-phone-components
Source0:	https://invent.kde.org/plasma/plasma-phone-components/-/archive/master/plasma-phone-components-master.tar.bz2
License:	GPLv2/LGPLv2/LGPLv2.1
Group:		Graphical desktop/KDE
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(KF5Akonadi)
BuildRequires:	cmake(KF5Libkdepim)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Sonnet)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5Wayland)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Activities)
BuildRequires:	cmake(KF5Baloo)
BuildRequires:	cmake(PkgConfig)
BuildRequires:	pkgconfig(gstreamer-1.0)
Requires:	plasma-workspace

%description
Plasma components for mobile phones

%prep
%autosetup -p1 -n %{name}-master
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/kwinwrapper
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%{_datadir}/kservices5/kwin-script-org.kde.phone.multitasking.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.activities.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.homescreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.krunner.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.panel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.taskpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/kwin/scripts/org.kde.phone.multitasking
%{_datadir}/metainfo/org.kde.phone.activities.appdata.xml
%{_datadir}/metainfo/org.kde.phone.krunner.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.activities
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.krunner
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%{_datadir}/plasma/shells/org.kde.plasma.phone
%{_datadir}/sounds/sitter/ohits.ogg
%{_datadir}/wayland-sessions/plasma-mobile.desktop
