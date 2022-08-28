#ifndef FUNCTIONS_H_
#define FUNCTIONS_H_

#include <cmath>
#include <stdexcept>

void egcd(int a, int b, int& gcd, int& x, int& y);

int modinv(int a, int m);

bool rootIsInt(int n, int r);

#endif // FUNCTIONS_H_