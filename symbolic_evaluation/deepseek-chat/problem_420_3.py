import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute square root of 5
sqrt5 = mp.sqrt(5)

# Calculate the first term: (3 - sqrt(5)) / 2
term1 = (3 - sqrt5) / 2

# Calculate the argument for the logarithm: (-1 + sqrt(5)) / 2
log_arg = (-1 + sqrt5) / 2

# Compute the second term: (1/2) * ln(log_arg)
term2 = 0.5 * mp.log(log_arg)

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))