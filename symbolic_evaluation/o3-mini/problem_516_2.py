import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate pi/2
half_pi = mp.pi / 2

# Subtract 1 to get the result
result = half_pi - 1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))