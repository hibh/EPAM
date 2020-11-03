def check_power_of_2(a: int) -> bool:
    if type(a) not in [int]:
        raise TypeError("a must be integer")
    if a < 2:
        return False
    return not (bool(a & (a - 1)))
