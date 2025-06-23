import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the numerator and denominator components
numerator = mp.mpf(3)
denominator = mp.mpf(16)

# Compute the fraction 3/16
fraction = numerator / denominator

# Multiply by pi to get the final result
result = fraction * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))