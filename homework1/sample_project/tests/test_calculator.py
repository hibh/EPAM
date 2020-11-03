import pytest
from calc import check_power_of_2


@pytest.mark.parametrize(
    ["value", "expected_result"], {(65536, True), (12, False), (2, True), (-10, False)}
)
def test_power_of_2(value: int, expected_result: bool):
    actual_result = check_power_of_2(value)

    assert actual_result == expected_result


def test_throw_exceptions_when_value_is_bool():
    with pytest.raises(TypeError) as ex:
        check_power_of_2(True)
    assert "a must be integer" in str(ex.value)


def test_throw_exceptions_when_value_is_string():
    with pytest.raises(TypeError) as ex:
        check_power_of_2("kawabanga")
    assert "a must be integer" in str(ex.value)


def test_throw_exceptions_when_value_is_float():
    with pytest.raises(TypeError) as ex:
        check_power_of_2(2.0)
    assert "a must be integer" in str(ex.value)
