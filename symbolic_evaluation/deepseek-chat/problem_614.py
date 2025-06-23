import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Evaluate the analytical expression: 1/2
result = mp.mpf(1) / 2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))