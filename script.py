#!/usr/bin/python3

from math import sqrt
from functions import *
from tables import *

"""
https://www.degruyter.com/document/doi/10.1515/jmc-2016-0046/html?lang=en
"""
def getPandQfromN(n):
    # r = p + q
    # Start r values at approximately 2sqrt(n)
    r_starting_guess = int(2*sqrt(n))

    # Table 2: n = 1 mod 100
    if n % 100 == 1:
        pass
    # Table 3: n = 11 mod 100
    # Table 4: n = 21 mod 100
    # Table 5: n = 31 mod 100
    # Table 6: n = 41 mod 100
    # Table 7: n = 51 mod 100
    # Table 8: n = 61 mod 100
    # Table 9: n = 71 mod 100
    # Table 23: n = 7 mod 10
    elif n % 10 == 7:
        constants = Table23(n)
        for i, [a, b] in enumerate(constants):
            k_i = int((r_starting_guess - b) / a)
            # Avoiding IndexError
            if i != len(constants) - 1:
                k_i1 = int((r_starting_guess - constants[i + 1][1]) / constants[i + 1][0])
                while not rootIsInt(n, k_i) and k_i != k_i1:
                    k_i += 1
                if rootIsInt(n, k_i):
                    r = a*k_i + b
                    pminusq = sqrt(r**2 - 4*n)
                    p = (r + (pminusq)) / 2
                    q = n / p
                    return p, q
            else:
                while not rootIsInt(n, k_i):
                    k_i += 1
                r = a*k_i + b
                pminusq = sqrt(r**2 - 4*n)
                p = (r + (pminusq)) / 2
                q = n / p
                return p, q
            print(k_i)

def main():
    e = 65537
    n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
    c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
    d = modinv(e, n)
    decrypt = (c**d) % n
    print("decrypt", decrypt)
    p, q = getPandQfromN(n)
    print(p)
    print(q)

if __name__ == "__main__":
    main()