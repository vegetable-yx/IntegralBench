import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate arcsin(1/4)
asin_val = mp.asin(1/4)

# Compute the first term: (pi/2) * arcsin(1/4)
term1 = (mp.pi / 2) * asin_val

# Compute the second term: (arcsin(1/4))^2 / 2
term2 = (asin_val ** 2) / 2

# Sum both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))