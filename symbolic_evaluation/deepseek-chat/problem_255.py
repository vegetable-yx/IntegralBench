import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the value of pi
pi_value = mp.pi

# Compute numerator: 3 * pi
numerator = 3 * pi_value

# Compute the final result: (3 * pi) / 2
result = numerator / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))