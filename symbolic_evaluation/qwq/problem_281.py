import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the hyperbolic sine of 4
sinh_4 = mp.sinh(4)

# Multiply the components to get final result
result = sqrt_pi * sinh_4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))