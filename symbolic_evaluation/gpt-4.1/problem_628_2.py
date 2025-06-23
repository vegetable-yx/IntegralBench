import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression simplifies to: -π/8 - 1/4
# Calculate each part separately
pi_term = -mp.pi / 8
rational_term = -mp.mpf(1) / 4

# Combine the terms
result = pi_term + rational_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))