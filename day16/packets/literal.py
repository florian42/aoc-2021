from dataclasses import dataclass

import more_itertools

from day16.utils import bits_to_int


@dataclass
class Literal:
    data: str
    version: str
    type_id: 4

    @classmethod
    def decode_packet(cls, bits: str):
        version = bits_to_int(bits[:3])
        type_id = bits_to_int(bits[3:6])
        return Literal(data=bits[6:], version=version, type_id=type_id)

    def decode_literal_value_data(self):
        bit_value = self._get_literal_value_bits()
        return bits_to_int(bit_value)

    def _get_literal_value_bits(self):
        num_bits = []
        for chunk in more_itertools.chunked(self.data, 5):
            start = chunk[0]
            num = chunk[1:]
            print(num)
            num_bits.extend(num)
            if start == "0":
                return "".join(num_bits)
