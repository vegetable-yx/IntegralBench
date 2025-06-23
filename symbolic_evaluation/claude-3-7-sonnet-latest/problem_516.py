import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute π (pi) using mpmath constant
pi_val = mp.pi

# Calculate π/2
pi_over_2 = pi_val / 2

# Subtract 1 from π/2
result = pi_over_2 - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))