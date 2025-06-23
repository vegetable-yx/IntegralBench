import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 5
sqrt5 = mp.sqrt(5)

# Compute first term: (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Compute logarithm argument: (sqrt(5) + 1)/2
log_arg = (sqrt5 + 1) / 2

# Compute second term: (1/2) * ln(log_arg)
term2 = 0.5 * mp.log(log_arg)

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))