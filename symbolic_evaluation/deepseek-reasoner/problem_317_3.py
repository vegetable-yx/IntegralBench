import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate 2π term
two_pi = 2 * mp.pi

# Combine terms in numerator: π² + 2π - 16
numerator = pi_sq + two_pi - 16

# Calculate denominator: √2
sqrt2 = mp.sqrt(2)

# Final calculation: (π² + 2π - 16)/√2
result = numerator / sqrt2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))