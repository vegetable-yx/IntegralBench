import mpmath as mp
# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate π/2 using mpmath's pi constant
pi_half = mp.pi / 2

# Compute the final result by subtracting π/2 from 2
result = 2 - pi_half

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))