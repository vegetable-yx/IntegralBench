import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π/4 using mpmath's pi constant
pi_over_4 = mp.pi / 4

# Calculate 1/2 using mpmath's floating point representation
half = mp.mpf(1)/2

# Compute the final result by subtracting 1/2 from π/4
result = pi_over_4 - half

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))