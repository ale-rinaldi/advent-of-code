#!/usr/bin/perl
use strict;
use warnings;

open(FH, '<', "d1-input.txt") or die $!;

my $result = 0;

while (<FH>){
    $_ =~ s/^\s+|\s+$//g;
    print "Current line: " . $_ . "\n";
    my %matches;
    while ($_ =~ /[0-9]/g) {
        my $position = $-[0];
        my $value = substr($_, $position, 1);
        $matches{$position} = $value;
    }
    while ($_ =~ /one/g) {
        my $position = $-[0];
        my $value = 1;
        $matches{$position} = $value;
    }
    while ($_ =~ /two/g) {
        my $position = $-[0];
        my $value = 2;
        $matches{$position} = $value;
    }
    while ($_ =~ /three/g) {
        my $position = $-[0];
        my $value = 3;
        $matches{$position} = $value;
    }
    while ($_ =~ /four/g) {
        my $position = $-[0];
        my $value = 4;
        $matches{$position} = $value;
    }
    while ($_ =~ /five/g) {
        my $position = $-[0];
        my $value = 5;
        $matches{$position} = $value;
    }
    while ($_ =~ /six/g) {
        my $position = $-[0];
        my $value = 6;
        $matches{$position} = $value;
    }
    while ($_ =~ /seven/g) {
        my $position = $-[0];
        my $value = 7;
        $matches{$position} = $value;
    }
    while ($_ =~ /eight/g) {
        my $position = $-[0];
        my $value = 8;
        $matches{$position} = $value;
    }
    while ($_ =~ /nine/g) {
        my $position = $-[0];
        my $value = 9;
        $matches{$position} = $value;
    }
    my @keys = sort { $a <=> $b } keys %matches;
    print "Matches:\n";
    foreach my $key (@keys) {
        print $key . " => " . $matches{$key} . "\n";
    }
    my $min_key = $keys[0];
    my $max_key = $keys[-1];
    my $first_match = $matches{$min_key};
    my $last_match = $matches{$max_key};
    my $lresult = int($first_match . $last_match);
    $result += $lresult;
    print "Current result: " . $lresult . "\n";
    print "-----------\n"
}
print "Global result: " . $result . "\n";

close(FH);
