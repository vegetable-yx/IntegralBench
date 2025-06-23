import mpmath as mp
mp.dps = 15

# Calculate the rational number part: -1/4
rational_part = mp.mpf(-1)/4

# Calculate the pi-related term: -π/8
pi_term = -mp.pi/8

# Combine both terms
result = rational_part + pi_term

print(mp.nstr(result, n=10))