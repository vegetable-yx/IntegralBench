import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate natural logarithm of 3
log_term = mp.log(3)

# Calculate π/4
pi_term = mp.pi / 4

# Sum the two terms
result = log_term + pi_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))