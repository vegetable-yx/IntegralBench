import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel function of the first kind, order 1 at 2
bessel_val = mp.besseli(1, 2)

# Multiply the result by 8
result = 8 * bessel_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))