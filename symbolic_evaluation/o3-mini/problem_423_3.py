import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant integer 99
# Assign the constant value to result
result = mp.mpf(99)

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))