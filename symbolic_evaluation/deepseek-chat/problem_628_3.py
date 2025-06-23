import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define pi constant
pi_val = mp.pi

# Calculate one-eighth of pi
eighth_pi = pi_val / 8

# Apply negative sign to get final result
result = -eighth_pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))