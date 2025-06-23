import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator
numerator = mp.mpf(-1)
denominator = mp.mpf(16)

# Calculate the result: -1/16
result = numerator / denominator

# Print the result to 10 significant digits
print(mp.nstr(result, n=10))