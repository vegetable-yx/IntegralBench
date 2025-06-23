import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the first term: 2/3
term1 = mp.mpf(2) / mp.mpf(3)

# Calculate the second term: π/8
term2 = mp.pi / mp.mpf(8)

# Compute the result: term1 - term2
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))