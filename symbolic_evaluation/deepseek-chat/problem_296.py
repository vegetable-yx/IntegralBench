import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Calculate the first term: 4/3
term1 = mp.mpf(4) / mp.mpf(3)

# Calculate the denominator for the second term: 3 * pi
denom = mp.mpf(3) * mp.pi

# Calculate the second term: 8 / (3 * pi)
term2 = mp.mpf(8) / denom

# Combine the terms: (4/3) - (8/(3*pi))
result = term1 - term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))