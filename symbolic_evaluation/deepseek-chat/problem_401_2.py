import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: 1/2
# This is a simple rational number
result = mp.mpf(1) / mp.mpf(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))