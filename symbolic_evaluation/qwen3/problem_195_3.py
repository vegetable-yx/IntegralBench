import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2 using mpmath's pi constant
pi_half = mp.pi / 2

# Compute the final result: 2 - π/2
result = 2 - pi_half

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))