from day16.packets.operator import Operator


class TestOperator:
    def test_decode_n_packets(self):
        packet = Operator("0000000001101010000001100100000100011000001100000")

        assert packet.decode_n_packets() == "123"
