import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 3π using mpmath's pi constant
three_pi = 3 * mp.pi

# Store final result and print with 10 decimal precision
result = three_pi
print(mp.nstr(result, n=10))