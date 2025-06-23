import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Define numerator and denominator using exact values
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform exact division operation
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))