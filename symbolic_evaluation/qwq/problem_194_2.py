import mpmath as mp
mp.dps = 15

# Calculate π squared
pi_sq = mp.pi ** 2

# Calculate 6π term
six_pi = 6 * mp.pi

# Calculate 12√3 term
twelve_sqrt3 = 12 * mp.sqrt(3)

# Combine terms in numerator
numerator = pi_sq - six_pi + twelve_sqrt3

# Final result by dividing numerator by 60
result = numerator / 60

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))