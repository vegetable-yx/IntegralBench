import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Define the components of the fraction
numerator = 1
denominator = 2

# Calculate the exact fraction using arbitrary precision
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))