import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/3
pi_over_3 = mp.pi / 3

# Compute natural logarithm of π/3
log_value = mp.log(pi_over_3)

# Multiply by 2 to get final result
result = 2 * log_value

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))