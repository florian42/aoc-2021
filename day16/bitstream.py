from dataclasses import dataclass


@dataclass
class Bitstream:
    bits: str
    current_position: int = 0

    def decode_one_packet(self):
        version = self.decode_int(3)
        type_id = self.decode_int(3)
        data = self.decode_packet_data(type_id)
        return version, type_id, data

    def decode_packet_data(self, type_id: int):
        if type_id == 4:
            return self.decode_literal_value_data()
        return self.decode_operator_data()

    def decode_int(self, number_of_bits):
        return int(self.get_group(number_of_bits), 2)

    def get_group(self, number_of_bits):
        result = self.bits[
            self.current_position : self.current_position + number_of_bits
        ]
        self.current_position += number_of_bits
        return result

    def decode_literal_value_data(self) -> int:
        group = self.get_group(5)
        bits = ""
        while group is not None:
            bits += group[1:]
            group = None if group[0] == "0" else self.get_group(5)
        return int(bits, 2)

    def decode_operator_data(self):
        length_of_type = self.decode_int(1)

        if length_of_type == 1:
            return self._decode_operator_packets_packets_by_count(self.decode_int(11))

        return self._decode_operator_packets_by_length(self.decode_int(15))

    def _decode_operator_packets_packets_by_count(self, count: int):
        return [self.decode_one_packet() for _ in range(count)]

    def _decode_operator_packets_by_length(self, length: int):
        end = self.current_position + length
        packets = []

        while self.current_position < end:
            packets.append(self.decode_one_packet())

        return packets
