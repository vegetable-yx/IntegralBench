import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the modified Bessel function of the first kind, order 0 at 6
bessel_val = mp.besseli(0, 6)

# Calculate π divided by 3
pi_over_3 = mp.pi / 3

# Multiply to get the final result
result = pi_over_3 * bessel_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))