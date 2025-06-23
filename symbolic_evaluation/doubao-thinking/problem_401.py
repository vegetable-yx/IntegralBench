import mpmath as mp

# Set internal decimal precision to 15 for reliable calculations
mp.dps = 15

# Calculate the analytical expression: 1/2
result = mp.mpf(1) / 2

# Output the result with exactly 10 decimal places
print(mp.nstr(result, n=10))