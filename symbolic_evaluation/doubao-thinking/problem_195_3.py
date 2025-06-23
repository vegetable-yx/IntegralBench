import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π divided by 2
pi_over_2 = mp.pi / 2

# Compute the final result by subtracting π/2 from 2
result = 2 - pi_over_2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))