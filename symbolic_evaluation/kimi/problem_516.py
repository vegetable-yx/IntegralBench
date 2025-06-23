import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute pi/2
half_pi = mp.pi / 2

# Subtract 1
result = half_pi - 1

# Print result to 10 decimal places
print(mp.nstr(result, n=10))