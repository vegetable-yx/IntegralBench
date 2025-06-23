import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Calculate pi squared
pi_sq = mp.pi ** 2

# Multiply by 4: 4 * pi^2
numerator = 4 * pi_sq

# Divide by 3 and apply negative sign: - (4 * pi^2) / 3
result = -numerator / 3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))