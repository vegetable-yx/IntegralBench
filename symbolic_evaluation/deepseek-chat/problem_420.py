import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the first term: (3 - sqrt(5)) / 2
term1 = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (sqrt(5) - 1) / 2
log_arg = (sqrt5 - 1) / 2

# Compute the logarithm of the argument
log_val = mp.log(log_arg)

# Compute the second term: (1/2) * ln((sqrt(5)-1)/2)
term2 = 0.5 * log_val

# Combine both terms: first term minus the second term
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))