import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute the Bessel function of the first kind of order 0 at z=1
j0_val = mp.besselj(0, 1)

# Multiply by pi to get the final result
result = mp.pi * j0_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))