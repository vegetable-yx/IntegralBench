import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate the factor: π * √2 / 8
factor = (mp.pi * mp.sqrt(2)) / 8

# Compute the modified Bessel function of the first kind, order 1 at x=0.5
bessel_term = mp.besseli(1, 0.5)

# Multiply the factor by the Bessel function result
result = factor * bessel_term

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))