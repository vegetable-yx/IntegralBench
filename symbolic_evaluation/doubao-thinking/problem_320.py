import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate π/2 directly using mpmath's pi constant
result = mp.pi / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))