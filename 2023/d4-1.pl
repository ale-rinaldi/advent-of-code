#!/usr/bin/perl
use strict;
use warnings;

sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

open(FH, '<', "d4-input.txt") or die $!;

my $result = 0;

while(<FH>){
    $_ = trim($_);
    my @splitted = split(':', $_);
    my @splittedNumbers = split('\|', trim($splitted[1]));
    my @winningNumbers = split(' ', trim($splittedNumbers[0]));
    my @numbers = split(' ', trim($splittedNumbers[1]));
    my $cardResult = 0;
    for my $i (0 .. $#numbers){
        if($numbers[$i] ~~ @winningNumbers){
            if($cardResult == 0){
                $cardResult = 1;
            } else {
                $cardResult *= 2;
            }
        }
    }
    print "Card result: $cardResult\n";
    $result += $cardResult;
}

print "Result: $result\n";