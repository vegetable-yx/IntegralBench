import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# The analytical expression is a constant: 1005
# Assign the constant value to the result variable
result = mp.mpf('1005')

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))