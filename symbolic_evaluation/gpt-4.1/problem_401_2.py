import mpmath as mp

# Set internal precision to 15 decimal places for reliable calculations
mp.dps = 15

# Calculate the analytical expression: 1/2
# This is a simple fraction that evaluates exactly to 0.5
result = mp.mpf(1) / 2

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))