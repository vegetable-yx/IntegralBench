import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the analytical expression: 1/2
# This is a simple fraction that can be directly evaluated
result = mp.mpf(1) / mp.mpf(2)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))