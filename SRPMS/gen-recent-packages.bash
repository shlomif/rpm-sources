#!/bin/bash
ls -rt | perl -lne 'if (s/^perl-//) { s/-\d.*//; print "    \$(perl_latest \"$_\") \\"; }'
