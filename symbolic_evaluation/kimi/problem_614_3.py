import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value: 0.5833333333
# Assign the constant directly
result = mp.mpf('0.5833333333')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))