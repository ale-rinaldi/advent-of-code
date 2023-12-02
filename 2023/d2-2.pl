sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

open(FH, '<', "d2-input.txt") or die $!;

my $result = 0;

sub minimumRequiredCubes {
    my %minimum = ();
    my @parts = @_;
    foreach(@parts) {
        my %part = %$_;
        foreach(keys(%part)) {
            unless (exists $minimum{$_}) {
                $minimum{$_} = 0;
            }
            if ($minimum{$_} < $part{$_}) {
                $minimum{$_} = $part{$_};
            }
        }
    }
    return %minimum;
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
    my %requiredCubes = minimumRequiredCubes @parsedParts;
    my $power = 1;
    foreach(keys(%requiredCubes)) {
        $power *= $requiredCubes{$_};
    }
    print "Power: $power\n";
    $result += $power;
}
print "Result: $result\n";