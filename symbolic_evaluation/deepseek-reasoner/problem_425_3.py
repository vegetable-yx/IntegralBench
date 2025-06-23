import mpmath as mp
mp.dps = 15

# Define numerator and denominator with mpmath precision
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform the division
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))