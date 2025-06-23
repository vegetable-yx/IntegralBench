import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
j0 = mp.besselj(0, 1)

# Square the Bessel function value
j0_squared = j0 ** 2

# Compute 1 minus the squared Bessel function value
one_minus_j0_sq = 1 - j0_squared

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * one_minus_j0_sq

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))