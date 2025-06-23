import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# Define numerator and denominator
numerator = mp.mpf(5)
denominator = mp.mpf(16)

# Compute the fraction: 5 divided by 16
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))