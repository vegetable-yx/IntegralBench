import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 1
i0_value = mp.besseli(0, 1)

# Multiply by 2π to get the final result
result = 2 * mp.pi * i0_value

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))