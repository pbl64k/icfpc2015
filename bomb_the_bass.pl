#!/usr/bin/perl

use warnings;
use strict;

for my $x (int($ARGV[0])..int($ARGV[1]))
{
    print STDOUT "\nProcessing $x...\n";
    system("pypy solve.py problems/problem_$x.json");
    system("./sub.sh $x");
}

