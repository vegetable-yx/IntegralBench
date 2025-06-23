import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant: 4036
# Assign the constant value to the result variable
result = mp.mpf(4036)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))