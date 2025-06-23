import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Compute arcsin(1/4) - the inverse sine of 1/4
asin_val = mp.asin(1/mp.mpf(4))

# Compute first term: arcsin(1/4) * (pi/2)
term1 = asin_val * (mp.pi / 2)

# Compute second term: [arcsin(1/4)]^2 / 2
term2 = (asin_val ** 2) / 2

# Combine terms: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))