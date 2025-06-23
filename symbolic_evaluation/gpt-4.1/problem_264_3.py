import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate Bessel function of the first kind of order 0 at 1
j0_val = mp.besselj(0, 1)

# Calculate the (1 - J0(1)) component
one_minus_j0 = 1 - j0_val

# Multiply by π/4 to get final result
pi_over_4 = mp.pi / 4
result = pi_over_4 * one_minus_j0

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))