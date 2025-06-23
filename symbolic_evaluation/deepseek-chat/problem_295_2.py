import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the first term: 8/3
term1 = mp.mpf(8) / 3

# Calculate the second term: π²/12
pi_squared = mp.pi ** 2
term2 = pi_squared / 12

# Combine terms: result = 8/3 - π²/12
result = term1 - term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))