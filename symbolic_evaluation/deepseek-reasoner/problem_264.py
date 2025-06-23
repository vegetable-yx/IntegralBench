import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate J0(1) - Bessel function of first kind of order 0 at 1
j0_1 = mp.besselj(0, 1)

# Square the Bessel function result
j0_squared = j0_1 ** 2

# Calculate (1 - J0(1)^2)
one_minus_j0_sq = 1 - j0_squared

# Multiply by π/4 to get final result
result = (mp.pi / 4) * one_minus_j0_sq

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))