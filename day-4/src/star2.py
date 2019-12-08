#!/usr/bin/env python3

from password_checker import PasswordChecker


def find_password_candidates() -> list:
    range_min = 156218
    range_max = 652527
    candidates = []

    for i in range(range_min, range_max):
        if not PasswordChecker.digits_all_increase(i):
            continue
        if not PasswordChecker.has_adjacent_digits_strict(i):
            continue
        candidates.append(i)

    print("In total", len(candidates), "digits were found.")
    return candidates


find_password_candidates()
