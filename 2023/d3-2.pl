{
    package Part;

    sub new {
        my $class = shift;
        my $number = shift;
        my $row = shift;
        my $start = shift;
        my $end = shift;
        my $self = {
            _number => $number,
            _row => $row,
            _start => $start,
            _end => $end
        };
        bless $self, $class;
        return $self;
    }

    sub number {
        my ($self, $number) = @_;
        $self->{_number} = $number if defined($number);
        return $self->{_number};
    }

    sub row {
        my ($self, $row) = @_;
        $self->{_row} = $row if defined($row);
        return $self->{_row};
    }

    sub start {
        my ($self, $start) = @_;
        $self->{_start} = $start if defined($start);
        return $self->{_start};
    }

    sub end {
        my ($self, $end) = @_;
        $self->{_end} = $end if defined($end);
        return $self->{_end};
    }
}

{
    package Symbol;

    sub new {
        my $class = shift;
        my $name = shift;
        my $row = shift;
        my $position = shift;
        my $self = {
            _name => $name,
            _row => $row,
            _position => $position
        };
        bless $self, $class;
        return $self;
    }

    sub name {
        my ($self, $name) = @_;
        $self->{_name} = $name if defined($name);
        return $self->{_name};
    }

    sub row {
        my ($self, $row) = @_;
        $self->{_row} = $row if defined($row);
        return $self->{_row};
    }

    sub position {
        my ($self, $position) = @_;
        $self->{_position} = $position if defined($position);
        return $self->{_position};
    }
}

sub  trim { my $s = shift; $s =~ s/^\s+|\s+$//g; return $s };

open(FH, '<', "d3-input.txt") or die $!;

my $result = 0;
my $row = 0;

my @parts;
my @symbols;

sub collides {
    my $part = shift;
    my $symbol = shift;
    my $partNumber = $part->number;
    my $symbolName = $symbol->name;
    my $symbolRow = $symbol->row;
    my $symbolPosition = $symbol->position;
    if ($symbol->row > $part->row + 1 || $symbol->row < $part->row - 1) {
        my $partRow = $part->row;
        my $symbolRow = $symbol->row;
        next
    }
    for my $i ($part->start .. $part->end-1) {
        if ($i == $symbol->position || $i == $symbol->position + 1 || $i == $symbol->position - 1) {
            return 1;
        }
    }
    return 0;
}

while (<FH>){
    $_ = trim($_);
    while(/[0-9]+/g) {
        my $number = $&;
        my $start = $-[0];
        my $end = $+[0];
        print "Number: $number, row: $row, start: $start, end: $end\n";
        my $part = Part->new($number, $row, $start, $end);
        push(@parts, $part);
    }
    while(/[^0-9.]/g) {
        my $name = $&;
        my $pos = $-[0];
        print "Symbol: $name, row: $row, posizion: $pos\n";
        my $symbol = Symbol->new($name, $row, $pos);
        push(@symbols, $symbol);
    }
    $row++;
}

foreach my $symbol (@symbols) {
    my $name = $symbol->name;
    if ($name ne '*') {
        next;
    }
    my $symbolRow = $symbol->row;
    my $symbolPosition = $symbol->position;
    print "Symbol $symbolRow, $symbolPosition\n";
    my @collidingParts;
    for my $part (@parts) {
        my $number = $part->number;
        if (collides($part, $symbol)) {
            print "Part $number collides\n";
            push(@collidingParts, $part);
        }
    }
    print "Colliding parts: " . (scalar @collidingParts) . "\n";
    if ((scalar @collidingParts) == 2) {
        print "Symbol $symbolRow, $symbolPosition collides with two parts\n";
        $result += ($collidingParts[0]->number * $collidingParts[1]->number);
    }
}

print "Result: $result\n";
