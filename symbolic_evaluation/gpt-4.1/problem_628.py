import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the constant term: -1/4
term1 = mp.mpf(-1) / 4

# Calculate the pi term: -π/8
term2 = -mp.pi / 8

# Combine the terms to get the final result
result = term1 + term2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))