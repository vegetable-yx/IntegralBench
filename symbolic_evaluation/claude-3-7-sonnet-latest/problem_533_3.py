import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define numerator and denominator as exact fractions
numerator = mp.mpf(8)
denominator = mp.mpf(7)

# Compute the exact fraction
result = numerator / denominator

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))