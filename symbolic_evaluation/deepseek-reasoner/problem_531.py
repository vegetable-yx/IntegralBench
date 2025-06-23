import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator using mpmath types
numerator = mp.mpf(5)
denominator = mp.mpf(6)

# Perform exact division using mpmath operations
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))