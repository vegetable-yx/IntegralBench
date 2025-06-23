import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator using mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Perform exact division using mpmath operations
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))