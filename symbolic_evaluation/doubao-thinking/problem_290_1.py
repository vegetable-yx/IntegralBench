import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator using exact integer values
numerator = mp.mpf(4)
denominator = mp.mpf(3)

# Perform exact division
result = numerator / denominator

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))