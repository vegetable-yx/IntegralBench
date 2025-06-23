import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the analytical expression: (3 * pi) / 4
result = (3 * mp.pi) / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))