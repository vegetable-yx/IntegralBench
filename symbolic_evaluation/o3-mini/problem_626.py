import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2
pi_over_2 = mp.pi / 2

# Compute natural logarithm of π/2
result = mp.log(pi_over_2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))