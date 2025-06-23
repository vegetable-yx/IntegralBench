import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using exact mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Perform exact division operation
result = numerator / denominator

# Print result with 10 decimal place precision
print(mp.nstr(result, n=10))