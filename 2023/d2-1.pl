sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

open(FH, '<', "d2-input.txt") or die $!;

my $result = 0;

sub gamePartPossible {
    my $partRef = shift;
    my %part = %$partRef;
    my %state = (
        'red' => 12,
        'green' => 13,
        'blue' => 14,
    );
    foreach(keys(%part)) {
        print "Trying to remove $part{$_} $_\n";
        print "There are $state{$_} $_ left\n";
        if ($state{$_} < $part{$_}) {
            print "Not enough $_\n";
            return 0;
        }
        $state{$_} -= $part{$_};
    }
    return 1;
}

sub gamePossible {
    my @parts = @_;
    foreach(@parts) {
        unless (gamePartPossible $_) {
            return 0;
        }
    }
    return 1;
}

sub parseGamePart {
    my $part = shift;
    my @splittedPart = split(',', $part);
    my %parsedPart;
    foreach(@splittedPart) {
        $_ = trim($_);
        my @spaceSplittedPart = split(' ', $_);
        $parsedPart{@spaceSplittedPart[1]} = int(@spaceSplittedPart[0]);
    }
    return %parsedPart;

}

while (<FH>){
    my @colonSplitted = split(':', $_);
    my @gameIdSplitted = split(' ', $colonSplitted[0]);
    my $gameId = int(@gameIdSplitted[1]);
    my @parts = split(';', $colonSplitted[1]);
    my @parsedParts;
    print "Processing game $gameId\n";
    foreach (@parts) {
        my %parsedPart = parseGamePart $_;
        push(@parsedParts, \%parsedPart);
    }
    if (gamePossible @parsedParts) {
        print "Game $gameId is possible\n";
        $result += $gameId;
    } else {
        print "Game $gameId is not possible\n";
    }
}
print "Result: $result\n";