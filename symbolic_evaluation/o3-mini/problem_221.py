import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the analytical expression: (3 * π) / 16
# Step 1: Calculate the numerator (3 * π)
numerator = 3 * mp.pi

# Step 2: Divide the numerator by the denominator (16)
result = numerator / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))