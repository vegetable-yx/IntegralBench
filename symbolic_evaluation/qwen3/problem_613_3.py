import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define numerator and denominator with mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(5)

# Perform exact division using mpmath types
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))