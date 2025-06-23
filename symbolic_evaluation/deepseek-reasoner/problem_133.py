import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic cosine of 1
cosh_1 = mp.cosh(1)

# Compute the difference (cosh(1) - 1)
difference = cosh_1 - 1

# Multiply components for final result
result = 2 * sqrt2 * difference

# Print result with 10 decimal places
print(mp.nstr(result, n=10))