import mpmath as mp
mp.dps = 15

# Compute Bessel function J0 at 1
j0_value = mp.besselj(0, 1)

# Square the Bessel function value
j0_squared = j0_value ** 2

# Calculate (1 - J0^2(1))
one_minus_j0_sq = 1 - j0_squared

# Multiply by π/4 to get final result
pi_over_4 = mp.pi / 4
result = pi_over_4 * one_minus_j0_sq

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))