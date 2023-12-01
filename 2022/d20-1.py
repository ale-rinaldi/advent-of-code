with open("d20-input.txt") as f:
    data = f.read().splitlines()


class Number:
    number: int
    current_position: int

    def __init__(self, number, position):
        self.number = number
        self.current_position = position


class Mixer:
    def __init__(self, numbers):
        self.numbers = [Number(int(x), i) for i, x in enumerate(numbers)]
        self.position_to_number = {}
        for i, x in enumerate(self.numbers):
            self.position_to_number[i] = x
            if x.number == 0:
                self.zero_position = i
        self.list_length = len(self.numbers)


    def _on_update_position(self, number):
        self.position_to_number[number.current_position] = number
        if number.number == 0:
            self.zero_position = number.current_position

    def get_list(self):
        new_numbers = []
        for x in range(self.list_length):
            new_numbers.append(self.position_to_number[x])
        return [n.number for n in new_numbers]

    def move_number(self, number, shift):
        new_position = number.current_position + shift
        if shift < 0:
            while new_position <= 0:
                shift += self.list_length - 1
                new_position = number.current_position + shift
        else:
            while new_position >= self.list_length:
                shift -= self.list_length - 1
                new_position = number.current_position + shift
        if shift == 0:
            return

        if shift > 0:
            for other_number in self.numbers:
                if other_number == number:
                    continue
                if other_number.current_position > number.current_position and other_number.current_position <= new_position:
                    other_number.current_position -= 1
                    self._on_update_position(other_number)
        else:
            for other_number in self.numbers:
                if other_number == number:
                    continue
                if other_number.current_position >= new_position and other_number.current_position < number.current_position:
                    other_number.current_position += 1
                    self._on_update_position(other_number)
        number.current_position = new_position
        self._on_update_position(number)

    def get_at_position(self, position):
        position = position + self.zero_position
        while position >= self.list_length:
            position -= self.list_length
        return self.position_to_number[position].number

    def mix_cycle(self):
        for number in self.numbers:
            self.move_number(number, number.number)
        new_numbers = []
        for x in range(self.list_length):
            new_numbers.append(self.position_to_number[x])
        self.numbers = new_numbers


mixer = Mixer(data)
mixer.mix_cycle()
print(mixer.get_at_position(1000) + mixer.get_at_position(2000) + mixer.get_at_position(3000))
