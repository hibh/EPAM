"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
import itertools
from typing import List


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    count = 0
    cartesian_product = itertools.product(a, b, c, d)
    cartesian_list = list(cartesian_product)
    for each_list in cartesian_list:
        if sum(each_list) == 0:
            count += 1
    return count
