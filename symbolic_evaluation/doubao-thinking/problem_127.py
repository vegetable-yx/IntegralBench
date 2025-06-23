import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic cosine of 1
cosh_1 = mp.cosh(1)

# Compute the difference (cosh(1) - 1)
difference = cosh_1 - 1

# Multiply components together: 2 * sqrt(2) * (cosh(1) - 1)
result = 2 * sqrt2 * difference

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))