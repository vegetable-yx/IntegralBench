import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the denominator from the analytical expression
denominator = mp.mpf(55273350)

# Compute the reciprocal: 1 / denominator
result = mp.mpf(1) / denominator

# Print the result to exactly 10 significant digits
print(mp.nstr(result, n=10))