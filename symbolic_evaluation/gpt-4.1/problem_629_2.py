import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Compute the argument for the logarithm: 2024 divided by 24
fraction = mp.mpf(2024) / mp.mpf(24)

# Calculate the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))