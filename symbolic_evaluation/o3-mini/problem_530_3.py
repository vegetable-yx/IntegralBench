import mpmath as mp

# Set the decimal places for internal calculations
mp.dps = 15

# The analytical expression is a constant value: 1
result = mp.mpf(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))