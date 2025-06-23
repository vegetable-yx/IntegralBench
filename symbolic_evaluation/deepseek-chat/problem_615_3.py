import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# The analytical expression is the constant 2
result = mp.mpf(2)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))