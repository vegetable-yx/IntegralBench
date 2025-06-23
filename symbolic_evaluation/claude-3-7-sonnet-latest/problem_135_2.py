import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the constant: (3 * pi) / 4
# Step 1: Compute 3 times pi
three_pi = 3 * mp.pi

# Step 2: Divide by 4 to get final result
result = three_pi / 4

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))