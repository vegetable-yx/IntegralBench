import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the analytical expression: 1/2
result = mp.mpf(1) / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))