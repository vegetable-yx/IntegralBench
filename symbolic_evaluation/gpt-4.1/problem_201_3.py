import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the Bessel function of the first kind of order 1 at z=1
j1_value = mp.besselj(1, 1)

# Multiply the result by π
result = mp.pi * j1_value

# Print the final result rounded to exactly 10 decimal places
print(mp.nstr(result, n=10))