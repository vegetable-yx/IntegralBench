import mpmath as mp
mp.dps = 15

# Define numerator and denominator using exact values
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform exact division
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))