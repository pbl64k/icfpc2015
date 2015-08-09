#!/usr/bin/perl

use warnings;
use strict;

for my $x (int($ARGV[0])..int($ARGV[1]))
{
    print STDOUT "\nProcessing $x...\n";
    system("pypy final_solver.py -f problems/problem_$x.json ".
            '-p "necronomicon" -p "yogsothoth" -p "yuggoth" -p "ia! ia!" -p "r\'lyeh" -p "ei!"');
    system("./sub.sh $x");
}

