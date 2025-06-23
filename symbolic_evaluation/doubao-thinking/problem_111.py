import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Calculate pi squared
pi_squared = mp.pi ** 2

# Compute the first term: sqrt(2) * pi^2
term1 = sqrt2 * pi_squared

# Compute the second term: 8 * sqrt(2)
term2 = 8 * sqrt2

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))