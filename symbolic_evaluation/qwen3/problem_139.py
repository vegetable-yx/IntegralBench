import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate hyperbolic cosine of 2
cosh_value = mp.cosh(2)

# Subtract 1 from the hyperbolic cosine result
result = cosh_value - 1

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))