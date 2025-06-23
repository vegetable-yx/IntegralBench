import mpmath as mp

# Set internal decimal precision to 15 for reliable calculations
mp.dps = 15

# Calculate the analytical result: 1/4 = 0.25
result = mp.mpf(1) / mp.mpf(4)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))