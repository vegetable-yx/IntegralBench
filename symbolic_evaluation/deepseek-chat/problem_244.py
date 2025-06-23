import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi^4
pi_val = mp.pi
pi_squared = mp.power(pi_val, 2)
pi_fourth = mp.power(pi_squared, 2)

# Calculate numerator: 7 * pi^4
numerator = 7 * pi_fourth

# Calculate denominator
denominator = 240

# Compute the final result
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))