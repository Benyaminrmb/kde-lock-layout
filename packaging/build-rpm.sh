#!/usr/bin/bash
set -euo pipefail

root=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
work="$root/.build/rpmbuild"
mkdir -p "$work"/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS,tmp} "$root/dist"

cp -a "$root/src" "$root/systemd" "$root/README.md" "$root/LICENSE" "$work/SOURCES/"
rpmbuild -bb "$root/packaging/kde-lock-layout.spec" \
    --define "_topdir $work" \
    --define "_sourcedir $work/SOURCES" \
    --define "_builddir $work/BUILD" \
    --define "_tmppath $work/tmp" \
    --define "_rpmdir $root/dist"
