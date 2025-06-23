import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π/2 using mpmath's pi constant
pi_half = mp.pi / 2

# Subtract 1 from π/2 value
result = pi_half - 1

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))