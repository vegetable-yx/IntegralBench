import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi/3
pi_over_3 = mp.pi / 3

# Compute logarithm of pi/3
log_term = mp.log(pi_over_3)

# Multiply by 2 to get the final result
result = 2 * log_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))