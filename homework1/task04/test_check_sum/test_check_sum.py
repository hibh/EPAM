from typing import List

import pytest
from check_sum import check_sum_of_four


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, 0, 1, -1], [1, 0, -3, 2], [11, -4, 8, -3], [1, 2, 3, -4], 19),
        ([1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16, 17], 0),
        ([0], [0, 0], [0, 0, 0], [0, 0, 0, 0], 24),
        ([0], [0], [0], [0], 1),
    ],
)
def test_check_sum_of_four(
    a: List[int], b: List[int], c: List[int], d: List[int], expected_result: int
):

    actual_result = check_sum_of_four(a, b, c, d)
    assert actual_result == expected_result
