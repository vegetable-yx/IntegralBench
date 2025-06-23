import mpmath as mp

# Set internal decimal precision to 15 for accuracy
mp.dps = 15

# Calculate pi/2
half_pi = mp.pi / 2

# Compute the expression: 2 - pi/2
result = 2 - half_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))