import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 3π using mpmath's pi
three_pi = 3 * mp.pi

# Divide by 4 to get the final result
result = three_pi / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))