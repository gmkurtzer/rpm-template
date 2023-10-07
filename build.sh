#!/bin/sh

CURRENTDIR=`pwd`

if ! rpmbuild -ba --define "_topdir $CURRENTDIR" $CURRENTDIR/SPECS/*.spec; then
    echo
    echo "Failed to build RPM"
    exit 255
fi
