import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Define the analytical expression: 1/2
result = mp.mpf(1) / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))