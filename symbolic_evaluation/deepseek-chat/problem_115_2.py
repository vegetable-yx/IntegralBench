import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate pi/2
half_pi = mp.pi / 2

# Subtract 1
result = half_pi - 1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))