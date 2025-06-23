import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the modified Bessel function of the first kind I_1(2.0)
i1_value = mp.besseli(1, 2.0)

# Calculate the square root of 2
sqrt2 = mp.sqrt(2)

# Multiply components together: π * sqrt(2) * I_1(2.0)
result = mp.pi * sqrt2 * i1_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))