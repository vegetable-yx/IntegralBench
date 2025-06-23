import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Subtract 1 from the computed hyperbolic cosine value
result = cosh_2 - 1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))