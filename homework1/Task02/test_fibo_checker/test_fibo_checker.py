from typing import Sequence

import pytest
from fibo_checker import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ([1, 1, 2, 3], True),
        ([1, 0, 1], False),
        ([4], False),
        ([1], True),
        ([1, 1, 1], False),
    ],
)
def test_check_fib(value: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
