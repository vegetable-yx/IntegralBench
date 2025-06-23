import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the Bessel function of the first kind of order 0 at z=1
j0_val = mp.besselj(0, 1)

# Multiply by π to get the result
result = mp.pi * j0_val

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))