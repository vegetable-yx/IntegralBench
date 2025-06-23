import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 6
i0_6 = mp.besseli(0, 6)

# Compute the difference from 1
numerator = i0_6 - 1

# Divide by 3 to get the final result
result = numerator / 3

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))