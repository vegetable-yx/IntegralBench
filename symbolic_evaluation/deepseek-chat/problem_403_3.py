import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 5040
# Assign the constant value to the result
result = 5040

# Print the result with exactly 10 decimal places using mpmath's nstr formatting
print(mp.nstr(result, n=10))