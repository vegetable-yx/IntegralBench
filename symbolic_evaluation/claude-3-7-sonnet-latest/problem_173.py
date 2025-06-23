import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi_val = mp.pi

# Compute π cubed
pi_cubed = pi_val ** 3

# Divide by 192 to get final result
result = pi_cubed / 192

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))