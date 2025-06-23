import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical expression simplifies to the constant 1
result = 1.0

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))