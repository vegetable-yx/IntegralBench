import mpmath as mp
# Set precision to 15 decimal places for calculations
mp.dps = 15

# Define numerator and denominator using mpmath types
numerator = mp.mpf(1)
denominator = mp.mpf(12)

# Perform exact rational division
result = numerator / denominator

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))