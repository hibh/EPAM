from typing import List

import pytest
from maximal_subarray_sum import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [([-3, 2, 3, -1, -5, -3, -9, 5], 3, 5), ([-1, 9, -1], 3, 9)],
)
def test_find_maximal_subarray_sum(nums: List[int], k: int, expected_result: int):
    actual_result = find_maximal_subarray_sum(nums, k)
    assert actual_result == expected_result


def test_throw_exceptions_when_k_value_is_less():
    with pytest.raises(ValueError) as ex:
        find_maximal_subarray_sum([1], 3)
    assert "'k' must be less than 'nums'" in str(ex.value)
