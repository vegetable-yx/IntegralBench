import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the first term: (3 - sqrt(5)) / 2
first_term = (3 - sqrt5) / 2

# Compute the argument for the logarithm: (-1 + sqrt(5)) / 2
log_arg = (-1 + sqrt5) / 2

# Compute the logarithm term: (1/2) * ln(log_arg)
log_term = 0.5 * mp.log(log_arg)

# Combine the terms to get the final result
result = first_term - log_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))