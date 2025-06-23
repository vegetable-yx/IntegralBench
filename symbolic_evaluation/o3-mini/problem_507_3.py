import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical expression is a constant integer: 18
# Assign the constant value to the result variable
result = mp.mpf(18)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))