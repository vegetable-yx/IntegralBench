import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate numerator and denominator as arbitrary-precision floats
numerator = mp.mpf(4)
denominator = mp.mpf(5)

# Perform the division with high precision
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))