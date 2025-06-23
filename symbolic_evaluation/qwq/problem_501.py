import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Define the numerator and denominator
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Compute the exact fraction
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))