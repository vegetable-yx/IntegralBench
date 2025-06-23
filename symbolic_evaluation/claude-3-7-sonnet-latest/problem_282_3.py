import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic cosine of 2
cosh2 = mp.cosh(2)

# Multiply the two results
result = sqrt2 * cosh2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))