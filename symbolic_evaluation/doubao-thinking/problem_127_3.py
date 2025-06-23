import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic cosine of 1
cosh_1 = mp.cosh(1)

# Compute the (cosh(1) - 1) term
cosh_term = cosh_1 - 1

# Multiply by 2*sqrt(2)
numerator = 2 * sqrt2 * cosh_term

# Divide by pi to get final result
result = numerator / mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))