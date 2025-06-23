import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute inverse hyperbolic sine of 2
arcsinh_2 = mp.asinh(2)

# Square the inverse hyperbolic sine result
arcsinh_squared = arcsinh_2 ** 2

# Multiply by pi/8 to get final result
result = (mp.pi / 8) * arcsinh_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))