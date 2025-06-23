import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate π/2 directly using mpmath's constant
result = mp.pi / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))