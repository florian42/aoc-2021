from dataclasses import dataclass


@dataclass
class Bitstream:
    bits: str
    pos: int = 0

    def decode_int(self, number_of_bits):
        result = int(self.bits[self.pos : self.pos + number_of_bits], 2)
        self.pos += number_of_bits
        return result

    def get_group(self, number_of_bits):
        result = self.bits[self.pos : self.pos + number_of_bits]
        self.pos += number_of_bits
        return result

    def decode_one_packet(self):
        version = self.decode_int(3)
        type_id = self.decode_int(3)
        data = self.decode_literal_value_data()
        return version, type_id, data

    def decode_literal_value_data(self):
        group = self.get_group(5)
        bits = ""
        while group is not None:
            bits += group[1:]
            next = self.get_group(5)
            if next[0] == "0":
                group = None
                bits += next[1:]
            else:
                group = next

        return int(bits, 2)
