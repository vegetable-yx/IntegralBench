import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the expression: (4 * pi) / 3
# Step 1: Multiply 4 by pi
four_pi = 4 * mp.pi

# Step 2: Divide the result by 3
result = four_pi / 3

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))