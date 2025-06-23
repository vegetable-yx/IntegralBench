import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply pi squared by sqrt(2)
pi_sq_sqrt2 = pi_sq * sqrt2

# Multiply by 3
numerator = 3 * pi_sq_sqrt2

# Divide by 256 to get the final result
result = numerator / 256

# Print result with 10 decimal places
print(mp.nstr(result, n=10))