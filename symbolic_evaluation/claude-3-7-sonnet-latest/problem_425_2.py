import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define numerator and denominator
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Compute the fraction: 128 / 153
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))