import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π^3
pi_cubed = mp.pi ** 3

# Compute 24π^3 term
term_24_pi3 = 24 * pi_cubed

# Compute 83π term
term_83_pi = 83 * mp.pi

# Calculate numerator: 24π^3 - 83π
numerator = term_24_pi3 - term_83_pi

# Final result calculation (divided by 512)
result = numerator / 512

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))