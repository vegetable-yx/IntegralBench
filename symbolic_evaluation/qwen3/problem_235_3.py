import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define numerator and denominator
numerator = 16
denominator = 3

# Compute the result using high-precision division
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))