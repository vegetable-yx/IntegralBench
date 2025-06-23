import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Multiply by 11
numerator = 11 * pi_sq

# Divide by 18 to get the result
result = numerator / 18

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))