import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the modified Bessel function of the first kind, order 1 at 1.0
I1_value = mp.besseli(1, 1.0)

# Multiply by 2.0 * pi
result = 2.0 * mp.pi * I1_value

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))