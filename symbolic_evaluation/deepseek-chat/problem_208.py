import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π using mpmath constant
pi_val = mp.pi

# Calculate π^3
pi_cubed = mp.power(pi_val, 3)

# First term: π^3 divided by 384
term1 = pi_cubed / 384

# Second term: π divided by 64
term2 = pi_val / 64

# Final result: subtract the second term from the first
result = term1 - term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))