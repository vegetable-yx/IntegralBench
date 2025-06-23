import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the analytical expression: (3 * π) / 4
# Step 1: Multiply 3 by π
three_pi = 3 * mp.pi

# Step 2: Divide the result by 4
result = three_pi / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))