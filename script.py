#!/usr/bin/python3

from math import sqrt


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

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

"""
Check if sqrt(r^2 - 4n) is an integer
"""
def rootIsInt(n, r):
    try:
        isInt = isinstance(sqrt(r**2 - 4*n), int)
        return isInt
    except ValueError:
        return False

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
    decrypt = (c^d) % n
    print("decrypt", decrypt)
    p, q = getPandQfromN(n)
    print(p)
    print(q)

if __name__ == "__main__":
    main()