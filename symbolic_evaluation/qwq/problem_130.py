import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic sine of 1
sinh_1 = mp.sinh(1)

# Multiply components to get final result
result = sqrt2 * sinh_1

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))