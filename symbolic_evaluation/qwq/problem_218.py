import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate π³/(54√3) term
pi_cubed = mp.pi ** 3
sqrt3 = mp.sqrt(3)
term1 = pi_cubed / (54 * sqrt3)

# Calculate (π/6)(ln2)² term
ln2 = mp.ln(2)
ln2_squared = ln2 ** 2
term2 = (mp.pi * ln2_squared) / 6

# Calculate -ln2 * Cl₂(π/3) term using Clausen function
clausen_value = mp.clsin(2, mp.pi/3)  # Clausen function of order 2
term3 = -ln2 * clausen_value

# Combine all terms
result = term1 + term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))