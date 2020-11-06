"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    ...


def get_rarest_char(file_path: str) -> str:
    with open(file_path) as f:
        counts = {}
        for line in f:
            for c in line.strip():
                counts[c] = counts.get(c, 0) + 1
    counts = sorted(counts.items(), key=lambda x: x[1])
    print(counts[0])


get_rarest_char("data.txt")


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...
