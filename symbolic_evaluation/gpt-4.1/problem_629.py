import mpmath as mp

# Set internal decimal precision to 15 to ensure accurate calculation
mp.dps = 15

# Calculate the fraction: 2024 / 24
fraction = mp.mpf(2024) / mp.mpf(24)

# Compute the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))