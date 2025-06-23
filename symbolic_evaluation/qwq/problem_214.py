import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 0 at 1
j0_val = mp.besselj(0, 1)

# Multiply by π to get the final result
result = mp.pi * j0_val

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))