import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate π divided by 2
pi_half = mp.pi / 2

# Compute the final result by subtracting π/2 from 1
result = 1 - pi_half

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))