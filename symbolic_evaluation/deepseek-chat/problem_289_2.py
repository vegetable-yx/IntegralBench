import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute the modified Struve function of order 0 at x=1
struvel_0_1 = mp.struvel(0, 1)

# Calculate π/4
pi_over_4 = mp.pi / 4

# Multiply π/4 by the Struve function value
product = pi_over_4 * struvel_0_1

# Subtract 1/2 to get the final result
result = product - 0.5

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))