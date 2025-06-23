import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator using exact mpmath types
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Perform the division with high precision
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))