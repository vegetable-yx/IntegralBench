import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: 1/2
# This is a simple fraction, so we can compute it directly
result = mp.mpf(1) / 2

# Print the result to exactly 10 decimal places using mp.nstr
print(mp.nstr(result, n=10))