import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2 using mpmath's constant for pi
result = mp.pi / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))