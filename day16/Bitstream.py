from dataclasses import dataclass

import more_itertools


@dataclass
class Bitstream:
    bits: str

    def _bits_to_int(self, bits: str):
        return int(bits, 2)

    def decode_packet(self):
        version = self._bits_to_int(self.bits[:3])
        type_id = self._bits_to_int(self.bits[3:6])
        data = self.decode_literal_value_data(self.bits[6:])
        return version, type_id, data

    def decode_literal_value_data(self, data: str):
        bit_value = self._get_literal_value_bits(data)
        return self._bits_to_int(bit_value)

    def _get_literal_value_bits(self, data: str):
        num_bits = []
        for chunk in more_itertools.chunked(data, 5):
            start = chunk[0]
            num = chunk[1:]
            num_bits.extend(num)
            if start == "0":
                return "".join(num_bits)
