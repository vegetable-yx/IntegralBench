import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Compute π raised to the third power
pi_cubed = pi_val**3

# Divide the result by 8
result = pi_cubed / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))