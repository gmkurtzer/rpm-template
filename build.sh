#!/bin/sh

CURRENTDIR=`pwd`
NAME=`basename "$CURRENTDIR"`

if ! test -f "SPECS/$NAME.spec"; then
    echo "ERROR: no specfile found in '$CURRENTDIR/$NAME'"
    exit 1
fi

if ! rpmbuild -ba --define "_topdir $CURRENTDIR" "SPECS/$NAME.spec"; then
    echo
    echo "Failed to build RPM"
    exit 255
fi
