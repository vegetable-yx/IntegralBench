import mpmath as mp
mp.dps = 15

# Define numerator and denominator using mpmath types
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform exact fraction division
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))