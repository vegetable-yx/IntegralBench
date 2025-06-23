import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using arbitrary precision
numerator = mp.mpf(1)
denominator = mp.mpf(2)

# Perform exact division with mpmath types
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))