import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the modified Bessel function of the first kind of order 0 at 1
i0 = mp.besseli(0, 1)

# Compute the modified Bessel function of the first kind of order 1 at 1
i1 = mp.besseli(1, 1)

# Calculate the difference and multiply by 2
result = 2 * (i0 - i1)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))