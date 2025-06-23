import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate 506π using direct multiplication
coefficient = 506
result = coefficient * mp.pi  # Multiply coefficient by mpmath's pi constant

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))