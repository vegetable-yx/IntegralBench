import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator using exact mpmath types
numerator = mp.mpf(4)
denominator = mp.mpf(3)

# Perform exact division using mpmath types
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))