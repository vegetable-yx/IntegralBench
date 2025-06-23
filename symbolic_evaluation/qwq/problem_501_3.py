import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate numerator and denominator using mpmath types
numerator = mp.mpf(2)
denominator = mp.mpf(5)

# Perform exact division using mpmath
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))