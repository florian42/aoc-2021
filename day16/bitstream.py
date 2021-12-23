from dataclasses import dataclass

from day16.packets.literal import Literal
from day16.utils import bits_to_int


@dataclass
class Bitstream:
    bits: str

    def decode_packet(self):
        literal = Literal.decode_packet(bits=self.bits)
        return literal.version, literal.type_id, literal.decode_literal_value_data()
