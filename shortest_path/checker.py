#!/usr/bin/env python3
"""
checker.py - Checker untuk soal Shortest Path.
Output hanya satu bilangan bulat (atau -1), cukup cek kesamaan teks.
Tapi checker ini memudahkan integrasi dengan run_tests.py.

Usage: python3 checker.py <input.in> <expected.out> <actual.out>
Returns: 0 jika benar, 1 jika salah
"""
import sys

def check(input_file, expected_file, actual_file):
    with open(expected_file) as f:
        expected = f.read().strip()
    with open(actual_file) as f:
        actual = f.read().strip()

    try:
        exp_val = int(expected)
        act_val = int(actual)
    except ValueError:
        print(f"CHECKER ERROR: Output bukan bilangan bulat. Expected='{expected}', Actual='{actual}'")
        return 1

    if exp_val == act_val:
        return 0
    else:
        print(f"WRONG: expected={exp_val}, got={act_val}")
        return 1

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <input.in> <expected.out> <actual.out>")
        sys.exit(2)
    sys.exit(check(sys.argv[1], sys.argv[2], sys.argv[3]))
