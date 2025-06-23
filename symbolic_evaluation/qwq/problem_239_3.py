import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate modified Bessel function of the first kind at 2 with order 1
bessel_term = mp.besseli(1, 2)

# Multiply by 2 according to the formula
result = 2 * bessel_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))