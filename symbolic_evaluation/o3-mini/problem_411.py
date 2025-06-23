import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# The analytical expression simplifies to the constant 1
result = mp.mpf(1)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))