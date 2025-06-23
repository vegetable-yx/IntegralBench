import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 0 at 3
bessel_value = mp.besseli(0, 3)

# Multiply by pi to get the final result
result = mp.pi * bessel_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))