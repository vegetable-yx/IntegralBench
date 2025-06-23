import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate Bessel function of the first kind of order 2 at 2
j2_value = mp.besselj(2, 2)

# Multiply by 2 to get final result
result = 2 * j2_value

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))