import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/2 using mpmath's constant
pi_half = mp.pi / 2

# Assign final result
result = pi_half

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))