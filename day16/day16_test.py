import pytest

from day16.bitstream import Bitstream
from day16.day16 import parse, evaluate_packet


def test_parse():
    assert parse("D2FE28") == "110100101111111000101000"


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("C200B40A82", 3),
        ("04005AC33890", 54),
        ("880086C3E88112", 7),
        ("CE00C43D881120", 9),
    ],
)
def test_evaluate(test_input, expected):
    stream = Bitstream(parse(test_input))
    packet = stream.decode_one_packet()
    result = evaluate_packet(packet)

    assert result == expected
