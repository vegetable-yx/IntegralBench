import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator as exact mpmath values
numerator = mp.mpf(15)
denominator = mp.mpf(16)

# Perform the division using high-precision arithmetic
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))