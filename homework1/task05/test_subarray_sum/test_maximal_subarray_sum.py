from typing import List

import pytest
from maximal_subarray_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"], [([1, 3, -1, -3, 5, 3, 6, 7], 3, 16)]
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == expected_result
