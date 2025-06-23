import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 2
i0_2 = mp.besseli(0, 2)

# Compute numerator (1 - I0(2))
numerator = 1 - i0_2

# Calculate final result by dividing numerator by 2
result = numerator / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))