#!/usr/bin/perl
use warnings;
use strict;
open(FO, ">store.yml");
for my $i (0..9) {
  my $j = $i + 1;
  print FO <<EOF;
add${i}:
  in: store/store${i}.dat
  out: store/store${j}.dat
EOF
}
close(FO);
