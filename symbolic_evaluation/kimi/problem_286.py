import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute (ln2 - 1) term
log_term = ln2 - 1

# Calculate π/4
pi_over_4 = mp.pi / 4

# Multiply components to get final result
result = pi_over_4 * log_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))