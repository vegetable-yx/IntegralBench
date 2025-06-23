import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant integer 2
result = 2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))