import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate arctan(2)
arctan2 = mp.atan(2)

# Calculate π/2 * arctan(2)
first_term = (mp.pi / 2) * arctan2

# Calculate ln(5)
ln5 = mp.log(5)

# Calculate (1/2) * ln(5)
second_term = 0.5 * ln5

# Combine the terms: first_term minus second_term
result = first_term - second_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))