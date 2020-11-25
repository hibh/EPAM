from slow_calculator import sum_f


"""
test sum of all arguments
calculation time has been asserted in main programm
"""


def test_sum_value():
    actual_result = sum_f()

    assert actual_result == 1025932
