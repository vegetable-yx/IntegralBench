import mpmath as mp
mp.dps = 15

# Calculate π² and divide by 32 for first term
pi_squared = mp.pi ** 2
term1 = pi_squared / 32

# Calculate π divided by 8 for second term
term2 = mp.pi / 8

# Calculate constant term 1/6 with high precision
term3 = mp.mpf(1)/6

# Combine all terms according to the formula
result = term1 - term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))