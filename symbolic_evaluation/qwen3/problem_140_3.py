import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of the first kind of order 1 at 2
i1_2 = mp.besseli(1, 2)

# Square the Bessel function result
i1_2_squared = i1_2 ** 2

# Multiply by 8 to get final result
result = 8 * i1_2_squared

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))