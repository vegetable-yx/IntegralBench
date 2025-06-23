import mpmath as mp

# Set internal decimal places for computation
mp.dps = 15

# Compute the analytical expression: π/2
result = mp.pi / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))