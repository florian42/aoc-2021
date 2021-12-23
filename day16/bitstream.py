from dataclasses import dataclass

from day16.packets.literal import Literal
from day16.utils import bits_to_int


@dataclass
class Bitstream:
    bits: str

    def decode_packet(self):
        version = bits_to_int(self.bits[:3])
        type_id = bits_to_int(self.bits[3:6])
        literal = Literal(self.bits[6:])
        return version, type_id, literal.decode_literal_value_data()
