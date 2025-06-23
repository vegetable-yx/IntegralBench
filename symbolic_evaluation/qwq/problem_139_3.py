import mpmath as mp
mp.dps = 15

# Calculate modified Bessel function of the first kind order 0 at 2
i0 = mp.besseli(0, 2)

# Subtract 1 from the Bessel function result
result = i0 - 1

# Print the final value with 10 decimal precision
print(mp.nstr(result, n=10))