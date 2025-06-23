import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate hyperbolic cosine of 3
cosh_3 = mp.cosh(3)

# Multiply components to get final result
result = sqrt_pi * cosh_3

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))