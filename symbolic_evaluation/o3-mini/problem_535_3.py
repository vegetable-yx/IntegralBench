import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: e raised to the power of 3
numerator = mp.exp(3)

# Define the denominator
denominator = 3

# Compute the result: e^3 divided by 3
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))