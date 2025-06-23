import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator and denominator
numerator = 17
denominator = 2

# Perform the division
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))