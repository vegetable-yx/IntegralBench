import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Calculate the modified Bessel function of the first kind of order 1 at 2
bessel_val = mp.besseli(1, 2)

# Multiply by π/4 to get the final result
result = (mp.pi / 4) * bessel_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))