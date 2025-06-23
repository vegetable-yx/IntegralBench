import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate numerator and denominator using exact values
numerator = mp.mpf(20)
denominator = mp.mpf(3)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))