import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define the numerator and denominator
numerator = 4
denominator = 3

# Compute the exact fraction value
result = mp.mpf(numerator) / mp.mpf(denominator)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))