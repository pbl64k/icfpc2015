#!/usr/bin/perl

use warnings;
use strict;

for my $x (0..24)
{
    print STDOUT "\nProcessing $x...\n";
    system("pypy solve.py problems/problem_$x.json");
    system("./sub.sh $x");
}

