from typing import Optional, List


class OverPacketEnd(Exception):
    pass


class BeforePacketBegin(Exception):
    pass


class InvalidOperatorType(Exception):
    pass


class Packet:
    version: int
    type_id: int
    literal_value: Optional[int] = None
    subpackets: list = []

    def __repr__(self):
        return f"<Packet version={self.version} type_id={self.type_id} literal_value={self.literal_value} subpackets_count={len(self.subpackets)}>"

    def get_version_sum(self):
        return self.version + sum([s.get_version_sum() for s in self.subpackets])

    def get_value(self):
        if self.type_id == 4:
            return self.literal_value
        elif self.type_id == 0:
            return sum([s.get_value() for s in self.subpackets])
        elif self.type_id == 1:
            res = self.subpackets[0].get_value()
            for s in self.subpackets[1:]:
                res = res * s.get_value()
            return res
        elif self.type_id == 2:
            return min([s.get_value() for s in self.subpackets])
        elif self.type_id == 3:
            return max([s.get_value() for s in self.subpackets])
        elif self.type_id == 5:
            return 1 if self.subpackets[0].get_value() > self.subpackets[1].get_value() else 0
        elif self.type_id == 6:
            return 1 if self.subpackets[0].get_value() < self.subpackets[1].get_value() else 0
        elif self.type_id == 7:
            return 1 if self.subpackets[0].get_value() == self.subpackets[1].get_value() else 0
        else:
            raise InvalidOperatorType


def hex_to_binary(input_hex):
    scale = 16
    num_of_bits = len(input_hex) * 4
    return bin(int(input_hex, scale))[2:].zfill(num_of_bits)


class PacketReader:
    def __init__(self, packet_binary: str):
        self.packet_binary = packet_binary
        self.current_offset = 0

    def read(self, bits_num: int):
        if self.current_offset + bits_num > len(self.packet_binary):
            raise OverPacketEnd
        start = self.current_offset
        end = start + bits_num
        self.current_offset = end
        return self.packet_binary[start:end]

    def read_int(self, bits_num: int):
        bits = self.read(bits_num)
        return int(bits, 2)

    def read_bool(self):
        bit = self.read(1)
        return bit == "1"

    def rewind(self, bit_nums: int):
        if self.current_offset - bit_nums < 0:
            raise BeforePacketBegin
        self.current_offset -= bit_nums


def parse_operator_subpackets(packet_reader: PacketReader) -> List[Packet]:
    result = []
    length_type_id = packet_reader.read_bool()
    if not length_type_id:
        subpackets_length = packet_reader.read_int(15)
        subpackets_payload = packet_reader.read(subpackets_length)
        subpackets_reader = PacketReader(subpackets_payload)
        ended = False
        while not ended:
            try:
                subpacket = parse_packet_from_reader(subpackets_reader)
                result.append(subpacket)
            except OverPacketEnd:
                ended = True
    else:
        subpackets_num = packet_reader.read_int(11)
        while len(result) < subpackets_num:
            result.append(parse_packet_from_reader(packet_reader))

    return result


def parse_literal_value(packet_reader: PacketReader):
    number_bin = ""
    others = True
    while others:
        others = packet_reader.read_bool()
        number_bin += packet_reader.read(4)
    return int(number_bin, 2)


def parse_packet_from_reader(packet_reader: PacketReader):
    packet = Packet()
    packet.version = packet_reader.read_int(3)
    packet.type_id = packet_reader.read_int(3)
    if packet.type_id == 4:
        packet.literal_value = parse_literal_value(packet_reader)
    else:
        packet.subpackets = parse_operator_subpackets(packet_reader)
    return packet


def parse_packet_binary(packet_binary: str):
    packet_reader = PacketReader(packet_binary)
    return parse_packet_from_reader(packet_reader)


def parse_packet_hex(packet_hex: str):
    return parse_packet_binary(hex_to_binary(packet_hex))


with open("d16-input.txt", "r") as f:
    input = f.read()

packet = parse_packet_hex(input.strip())
print(packet.get_value())
