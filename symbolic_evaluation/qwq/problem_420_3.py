import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute square root of 5
sqrt5 = mp.sqrt(5)

# Calculate first term: (3 - sqrt(5))/2
term1 = (3 - sqrt5) / 2

# Compute argument for logarithm: (sqrt(5) - 1)/2
log_argument = (sqrt5 - 1) / 2

# Calculate second term: 0.5 * natural log of the computed argument
term2 = 0.5 * mp.log(log_argument)

# Combine terms to get final result
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))