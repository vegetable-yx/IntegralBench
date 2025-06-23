import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical expression is a constant integer 18
result = 18

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))