import pytest
from armstrong_number import is_armstrong


"""
test a narcissistic number by known values
test exceptions by non integer type of input data
"""


@pytest.mark.parametrize(
    ["value", "expected_result"], [(9, True), (153, True), (154, False), (int(), True)]
)
def test_is_armstrong(value, expected_result):
    actual_result = is_armstrong(value)
    assert actual_result == expected_result


@pytest.mark.parametrize(["value"], [[0.0], ["string"], [str()], [True], [False]])
def test_throw_value_exception(value):
    with pytest.raises(Exception, match="Value is not integer"):
        is_armstrong(value)
