Name:           kde-lock-layout
Version:        1.0.0
Release:        1%{?dist}
Summary:        Switch KDE keyboard layout to English when the screen locks
License:        MIT
BuildArch:      noarch
Requires:       dbus-tools
Requires:       qt6-qttools

%description
A Plasma user service that switches the active keyboard layout to English
(US) when the screen locks.

%prep

%build

%install
install -Dpm0755 %{_sourcedir}/src/kde-lock-layout \
    %{buildroot}%{_libexecdir}/kde-lock-layout
install -Dpm0644 %{_sourcedir}/systemd/kde-lock-layout.service \
    %{buildroot}%{_userunitdir}/kde-lock-layout.service
install -Dpm0644 %{_sourcedir}/README.md \
    %{buildroot}%{_docdir}/%{name}/README.md
install -Dpm0644 %{_sourcedir}/LICENSE \
    %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%license %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md
%{_libexecdir}/kde-lock-layout
%{_userunitdir}/kde-lock-layout.service

%changelog
* Wed Sep 30 2026 KDE Lock Layout contributors <maintainers@example.org> - 1.0.0-1
- Initial package
