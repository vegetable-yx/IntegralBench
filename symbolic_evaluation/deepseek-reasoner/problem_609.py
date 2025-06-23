import mpmath as mp
# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π divided by 2
pi_half = mp.pi / 2

# Compute the final value by subtracting π/2 from 1
result = 1 - pi_half

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))