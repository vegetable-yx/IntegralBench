import mpmath as mp

# Set internal precision to 15 decimal places
mp.mp.dps = 15

# Calculate the analytical expression: 1/2
result = mp.mpf(1) / mp.mpf(2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))