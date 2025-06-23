import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind of order 1 at 2
bessel_val = mp.besseli(1, 2)

# Multiply by pi
product = mp.pi * bessel_val

# Divide by 2 to get the final result
result = product / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))