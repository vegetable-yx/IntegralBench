import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the analytical expression: 1/2
result = mp.mpf(1) / 2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))