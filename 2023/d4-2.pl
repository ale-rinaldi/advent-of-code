#!/usr/bin/perl
use strict;
use warnings;

{
    package Card;

    sub new {
        my $class = shift;
        my $winningNumbers = shift;
        my $numbers = shift;
        my $self = {
            _winningNumbers => $winningNumbers,
            _numbers => $numbers,
            _copies => 1,
        };
        bless $self, $class;
        return $self;
    }

    sub addCopies {
        my $self = shift;
        my $copies = shift;
        $self->{_copies} += $copies;
    }

    sub copies {
        my ($self, $copies) = @_;
        $self->{_copies} = $copies if defined($copies);
        return $self->{_copies};
    }

    sub getWinningCount {
        my $self = shift;
        my $winning = 0;
        my $winningNumbersRef = $self->{_winningNumbers};
        my $numbersRef = $self->{_numbers};
        my @winningNumbers = @$winningNumbersRef;
        my @numbers = @$numbersRef;
        for my $i (0 .. scalar @numbers){
            if($numbers[$i] ~~ @winningNumbers){
                $winning += 1;
            }
        }
        return $winning;
    }
}

sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

open(FH, '<', "d4-input.txt") or die $!;

my $result = 0;
my @cards;

while(<FH>){
    $_ = trim($_);
    my @splitted = split(':', $_);
    my @splittedNumbers = split('\|', trim($splitted[1]));
    my @winningNumbers = split(' ', trim($splittedNumbers[0]));
    my @numbers = split(' ', trim($splittedNumbers[1]));
    print "In main: @winningNumbers\n";
    my $card = Card->new(\@winningNumbers, \@numbers);
    push(@cards, $card);
}

my $cardIndex = 0;
foreach my $card (@cards) {
    print "Processing card with index $cardIndex\n";
    my $winning = $card->getWinningCount;
    print "Card $cardIndex has $winning winning numbers\n";
    for my $i ($cardIndex + 1 .. $cardIndex + 1 + $winning - 1) {
        my $thisCardCopies = $card->copies;
        print "Adding $thisCardCopies copies to card $i\n";
        $cards[$i]->addCopies($thisCardCopies);
        my $newCardCopies = $cards[$i]->copies;
        print "Card $i now has $newCardCopies copies\n";
    }
    $cardIndex++;
}

foreach my $card(@cards) {
    $result += $card->copies;
}

print "Result: $result\n";
