import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the given analytical expression (constant value 4036)
result = mp.mpf(4036)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))