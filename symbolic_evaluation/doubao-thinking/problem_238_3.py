import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator separately
numerator = mp.mpf(16)
denominator = mp.mpf(3)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))