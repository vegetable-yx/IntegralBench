import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define constant term
constant = mp.mpf(2)

# Calculate π/2
half_pi = mp.pi / 2

# Compute final result: 2 - π/2
result = constant - half_pi

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))