import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: 16/15
term1 = mp.mpf(16) / mp.mpf(15)

# Calculate the second term: pi squared divided by 24
pi_squared = mp.pi ** 2
term2 = pi_squared / mp.mpf(24)

# Combine the terms: term1 minus term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))