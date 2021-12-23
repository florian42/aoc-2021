from day16.bitstream import Bitstream


class TestBitstream:
    def test_decode_one_literal_packet(self):
        bit_stream = Bitstream("110100101111111000101000")

        version, result, data = bit_stream.decode_one_packet()
        assert (version, result, data) == (6, 4, 2021)

    def test_decode_operator_data(self):
        bit_stream = Bitstream(
            "11101110000000001101010000001100100000100011000001100000"
        )
        result = bit_stream.decode_one_packet()
        assert result == (7, 3, [(2, 4, 1), (4, 4, 2), (1, 4, 3)])
