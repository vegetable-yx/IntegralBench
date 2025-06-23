import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Compute the modified Bessel function of the first kind of order 0 at z=1
i0_val = mp.besseli(0, 1)

# Multiply: π * √2 * I₀(1)
result = mp.pi * sqrt2 * i0_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))