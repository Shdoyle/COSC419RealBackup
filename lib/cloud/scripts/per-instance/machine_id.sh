#!/bin/bash
CT=$(date +%s);
FT=$(stat /etc/machine-id -c %Y);
DIFF=$(expr $CT - $FT)
# record timestamp on machine-id for testing
# If /etc/machine_id is over 10m old on first-boot, delete it
if [ -f /etc/machine-id ]; then
    if [ $DIFF -lt 600 ]; then
        exit 0
    fi
rm -rf /etc/machine-id
fi

# systemd will use dbus uudigen if its there
# we need to reset this for Debain 9.
if which dbus-uuidgen &> /dev/null; then
    rm -rf /var/lib/dbus/machine-id
    dbus-uuidgen --ensure=/var/lib/dbus/machine-id
fi

if which systemd-machine-id-setup &> /dev/null; then
    rm -rf /etc/machine-id
    systemd-machine-id-setup
fi
