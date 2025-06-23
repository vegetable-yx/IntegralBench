import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator using high-precision floats
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform the division with high precision
result = numerator / denominator

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))