import mpmath as mp
mp.dps = 15

# Compute Bessel function J1(2)
j1 = mp.besselj(1, 2)

# Compute Bessel function J2(2)
j2 = mp.besselj(2, 2)

# Multiply the Bessel function values
product = j1 * j2

# Divide by 2 to get final result
result = product / 2

print(mp.nstr(result, n=10))