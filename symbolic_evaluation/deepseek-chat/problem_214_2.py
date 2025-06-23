import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at 1.0
j0_val = mp.besselj(0, 1.0)

# Multiply by π
result = mp.pi * j0_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))