from typing import List

import pytest
from common_and_rarest import major_and_minor_elem


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        (
            [
                "common",
                "legendary",
                "mythic",
                "common",
                "common",
                "rare",
                "common",
                "1",
            ],
            ("common", "legendary"),
        ),
    ],
)
def test_major_and_minor_elem(value: List, expected_result: tuple):
    actual_result = major_and_minor_elem(value)
    assert actual_result == expected_result


def test_major_and_minor_typeerror():
    with pytest.raises(TypeError, match="Input must be List"):
        major_and_minor_elem(1)
