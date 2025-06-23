import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 5
numerator = 5 * pi_sq

# Divide by 8 to get the result
result = numerator / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))