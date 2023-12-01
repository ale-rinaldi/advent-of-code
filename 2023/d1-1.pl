#!/usr/bin/perl
use strict;
use warnings;

open(FH, '<', "d1-input.txt") or die $!;

my $result = 0;

while(<FH>){
    print $_ . "\n";
    my @array = split(//, $_);
    my $lresult = 0;
    my $first = "";
    my $last = "";
    my $char;
    foreach $char (@array){
        if($char =~ /[0-9]/){
            if($first eq ""){
                $first = $char;
            }
            $last = $char;
        }
    }
    print "First: " . $first . "\n";
    print "Last: " . $last . "\n";
    $lresult = int($first . $last);
    $result += $lresult;
    print "Local: " . $lresult . "\n";
    print "Global: " . $result . "\n";
}

print $result . "\n";

close(FH);
