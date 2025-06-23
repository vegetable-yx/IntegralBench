import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Define the numerator
numerator = mp.mpf(4)

# Define the denominator
denominator = mp.mpf(5)

# Calculate the result of 4/5
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))