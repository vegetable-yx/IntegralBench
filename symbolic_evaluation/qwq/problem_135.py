import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 3π using mpmath's pi constant
three_pi = 3 * mp.pi

# Divide the result by 4 to get 3π/4
result = three_pi / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))