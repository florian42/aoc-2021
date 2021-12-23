from day16.bitstream import Bitstream


class TestBitstream:
    def test_decode_one_literal_packet(self):
        bit_stream = Bitstream("110100101111111000101000")

        version, result, data = bit_stream.decode_one_packet()
        assert (version, result, data) == (6, 4, 2021)
