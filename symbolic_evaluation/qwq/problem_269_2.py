import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π^3
pi_cubed = pi_value ** 3

# Compute 6π term
six_pi = 6 * pi_value

# Calculate numerator (π^3 - 6π)
numerator = pi_cubed - six_pi

# Final result by dividing numerator by 288
result = numerator / 288

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))