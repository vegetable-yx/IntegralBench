import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the first term: (3 - sqrt(5)) / 2
term1 = (3 - sqrt5) / 2

# Calculate the argument for the logarithm: (-1 + sqrt(5)) / 2
log_arg = (-1 + sqrt5) / 2

# Compute the natural logarithm of the argument
log_term = mp.log(log_arg)

# Compute the second term: - (1/2) * log_arg
term2 = -0.5 * log_term

# Combine the two terms to get the final result
result = term1 + term2  # Note: term2 is negative so we add it

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))