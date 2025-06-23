import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 1 at 2.0
bessel_val = mp.besseli(1, 2.0)

# Multiply by π to get the final result
result = mp.pi * bessel_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))