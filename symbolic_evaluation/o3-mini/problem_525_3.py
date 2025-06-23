import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Calculate the analytical expression: 1/2
result = mp.mpf(1) / mp.mpf(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))