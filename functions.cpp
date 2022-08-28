#include "functions.h"

void egcd(int a, int b, int& gcd, int& x, int& y) {
    x = 0;
    y = 1;
    int u = 1;
    int v = 0;

    while (a != 0) {
        int q = b / a;
        int r = b % a;
        int m = x - u * q;
        int n = y - v * q;
        b = a;
        a = r;
        x = u;
        y = v;
        u = m;
        v = n;
    }
    gcd = b;
}

int modinv(int a, int m) {
    int gcd, x, y;
    egcd(a, m, gcd, x, y);
    if (gcd != 1) {
        return 0;
    } else {
        return x % m;
    }
}

bool rootIsInt(int n, int r) {
    try {
        float k = sqrt(r*r - 4*n);
        return floor(k) == k;
    } catch(const std::domain_error& e) {
        return false;
    }
}