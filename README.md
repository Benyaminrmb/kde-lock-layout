# KDE Lock Layout

KDE Plasma 6 user service that switches the keyboard to English (US) when the
screen locks. This is useful when Persian or another layout was active before
locking. It works with Plasma's session D-Bus and is intended for Wayland or
X11 sessions.

## Fedora RPM install

Install the packaged release and enable the service for your user:

```sh
sudo dnf install https://github.com/Benyaminrmb/kde-lock-layout/releases/download/v1.0.0/kde-lock-layout-1.0.0-1.fc44.noarch.rpm
systemctl --user enable --now kde-lock-layout.service
```

The service starts when the Plasma graphical session starts. It only affects
the lock screen of the current logged-in session; SDDM's boot login screen has
its own keyboard configuration.

## Build the RPM from source

On Fedora, install the build tools and create the package:

```sh
sudo dnf install rpm-build
./packaging/build-rpm.sh
```

The resulting RPM is written to `dist/`.

## Remove

```sh
systemctl --user disable --now kde-lock-layout.service
sudo dnf remove kde-lock-layout
```

## How it works

The user service listens for `org.freedesktop.ScreenSaver.ActiveChanged(true)`.
When the screen locks, it asks KDE's `org.kde.KeyboardLayouts` D-Bus interface
for the configured layouts, finds the `us` entry by name, and activates it.
The layout index is looked up each time, so changing layout order does not
break the service.
