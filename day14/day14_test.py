from typing import Dict

import pytest

from day14.day14 import insert_pair


@pytest.mark.parametrize(
    "pair,pairs,expected",
    [
        ("NN", {"NN": "C"}, "NCNCB"),
        ("NC", {"NC": "B"}, "NNBCB"),
        ("CB", {"CB": "H"}, "NNCHB"),
    ],
)
def test_insert_pair_inserts_character_between_adjacent_chars(
    pair: str, pairs: Dict[str, str], expected: str
):
    result = insert_pair("NNCB", pair, pairs)

    assert result == expected
