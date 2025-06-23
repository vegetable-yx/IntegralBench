import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π (pi) using mpmath constant
pi_value = mp.pi

# Compute π/4
pi_over_4 = pi_value / 4

# Compute the constant term 1/2
one_half = mp.mpf(1)/2

# Combine the results: π/4 - 1/2
result = pi_over_4 - one_half

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))