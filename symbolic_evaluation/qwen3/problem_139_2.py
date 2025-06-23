import mpmath as mp
# Set decimal places for internal precision
mp.dps = 15
# Calculate hyperbolic cosine of 2
cosh_value = mp.cosh(2)
# Subtract 1 from the computed hyperbolic cosine value
result = cosh_value - 1
# Print the result to 10 decimal places
print(mp.nstr(result, n=10))