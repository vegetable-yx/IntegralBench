import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate the first term: 1/2
term1 = mp.mpf(1)/2

# Calculate the second term: π/8
term2 = mp.pi / 8

# Compute the result: (1/2) - (π/8)
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))