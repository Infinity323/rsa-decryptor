#!/usr/bin/python3

"""
Table 15: n = 39 mod 100
"""
def Table15(n, r_guess):
    # Hundreds Odd
    if int(n / 100) % 2 == 1:
        # 3 | n + 1
        if (n + 1) % 3 == 0:
            return [int((r_guess - 516) / 600),
                    int((r_guess - 84) / 600),
                    int((r_guess - 60) / 120)]
        # 3 ∤ n + 1
        else:
            return [int((r_guess - 116) / 600),
                    int((r_guess - 316) / 600),
                    int((r_guess - 284) / 600),
                    int((r_guess - 484) / 600),
                    int((r_guess - 20) / 120),
                    int((r_guess - 100) / 120)]
    # Hundreds Even
    else:
        # 3 | n + 1
        if (n + 1) % 3 == 0:
            return [int((r_guess - 216) / 600),
                    int((r_guess - 384) / 600),
                    int(r_guess / 120)]
        # 3 ∤ n + 1
        else:
            return [int((r_guess - 16) / 600),
                    int((r_guess - 416) / 600),
                    int((r_guess - 84) / 600),
                    int((r_guess - 584) / 600),
                    int((r_guess - 40) / 120),
                    int((r_guess - 80) / 120)]

"""
Table 23: n = 7 mod 10
"""
def Table23(n):
    # Tens Odd
    if int(n / 10) % 2 == 1:
        # 3 | n + 1
        if (n + 1) % 3 == 0:
            return [[60, 18],
                    [60, 42]]
        # 3 ∤ n + 1
        else:
            return [[60, 38],
                    [60, 58],
                    [60, 2],
                    [60, 22]]
    # Tens Even
    else:
        # 3 | n + 1
        if (n + 1) % 3 == 0:
            return [[60, 48],
                    [60, 12]]
        # 3 ∤ n + 1
        else:
            return [[60, 8],
                    [60, 28],
                    [60, 32],
                    [60, 52]]
