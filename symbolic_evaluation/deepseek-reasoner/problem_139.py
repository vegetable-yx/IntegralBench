import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate hyperbolic cosine of 2
cosh_2 = mp.cosh(2)

# Subtract 1 from the result
result = cosh_2 - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))