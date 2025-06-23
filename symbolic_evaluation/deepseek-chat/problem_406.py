import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the analytical expression: π/6
result = mp.pi / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))