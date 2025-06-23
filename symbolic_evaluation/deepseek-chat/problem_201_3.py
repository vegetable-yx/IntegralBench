import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at x=1
j1_val = mp.besselj(1, 1)

# Multiply the result by pi
result = mp.pi * j1_val

# Print the final result with exactly 10 significant digits
print(mp.nstr(result, n=10))