from typing import Tuple

import pytest
from find_min_max import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"], [("Test1.txt", (-2, 7)), ("Test2.txt", (-1, -1))]
)
def test_find_min_max(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
