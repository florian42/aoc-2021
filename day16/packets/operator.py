from dataclasses import dataclass

import more_itertools

from day16.packets.literal import Literal
from day16.utils import bits_to_int


@dataclass
class Operator:
    data: str

    def decode_n_packets(self):
        number_of_packets = bits_to_int(self.data[:11])
        chunks = more_itertools.chunked(self.data[11:], 11)
        return "".join(
            [
                str(
                    Literal.decode_packet(
                        "".join(next(chunks))
                    ).decode_literal_value_data()
                )
                for _ in range(number_of_packets)
            ]
        )
