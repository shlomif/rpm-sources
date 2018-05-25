#!/bin/bash

latest()
{
    ls "$1"-* | tail -1
}

# Numeric latest
nlat()
{
    ls "$1"-[0123456789].* | tail -1
}

perl_latest()
{
    latest "perl-$1"
}

rsync -v --inplace --progress --rsh=ssh --delete-after -a \
    --exclude 'PySolFC-cardsets*.src.rpm' \
    --exclude 'apache*.src.rpm' \
    --exclude 'htdig*.src.rpm' \
    --exclude '**/maven2*.src.rpm' \
    --exclude 'rpm-5*.src.rpm' \
    --exclude '*~' \
    . "${__HOMEPAGE_REMOTE_PATH}/open-source/packages/Mageia/SRPMS/"
