import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is -3π
# Assign constant multiplier
multiplier = -3

# Calculate the product: -3 * π
result = multiplier * mp.pi

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))