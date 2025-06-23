import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi divided by 4
pi_val = mp.pi  # Get the constant π
divisor = 4     # Denominator value for division
result = pi_val / divisor  # Calculate π/4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))