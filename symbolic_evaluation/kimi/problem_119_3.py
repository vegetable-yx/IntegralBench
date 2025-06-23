import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the term (2 - sqrt(2))
term = 2 - sqrt2

# Multiply pi squared by the term
numerator = pi_sq * term

# Divide by 6 to get the final result
result = numerator / 6

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))