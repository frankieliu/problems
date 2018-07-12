#!/usr/bin/perl -Tw

use strict;
use warnings;

my %in_use;
{
    local $ENV{PATH} = '/bin:/usr/bin';

    %in_use = map { $_ => 1 } split /\n/, qx(
        netstat -aunt          |\
        awk '{print \$4}'      |\
        grep :                 |\
        awk -F: '{print \$NF}'
    );
}

my ($port) = grep { not $in_use{$_} } 50_000 .. 59_999;

print "$port is available\n";
