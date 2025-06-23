import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate -3π using mpmath's pi constant
three_pi = 3 * mp.pi
result = -three_pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))