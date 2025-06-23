import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the analytical expression: π/4
result = mp.pi / 4

# Output the result to exactly 10 decimal places
print(mp.nstr(result, n=10))