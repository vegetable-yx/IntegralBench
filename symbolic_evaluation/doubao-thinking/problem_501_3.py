import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator and denominator separately
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform the division
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))