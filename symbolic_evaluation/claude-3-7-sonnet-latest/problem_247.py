import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 3
numerator = 3 * pi_sq

# Divide by 32 to get the result
result = numerator / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))