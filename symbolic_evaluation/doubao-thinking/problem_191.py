import mpmath as mp
mp.dps = 15

# Calculate components of the numerator
pi_squared = mp.pi ** 2
term_24pi = 24 * mp.pi
combined_terms = term_24pi - pi_squared - 48

# Compute full numerator by multiplying with pi
numerator = mp.pi * combined_terms

# Final calculation with denominator
denominator = 1152
result = numerator / denominator

print(mp.nstr(result, n=10))