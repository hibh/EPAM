import pytest
from calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"], {(65536, True), (12, False), (2, True), (-10, False)}
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result
