import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate fundamental constants and values
pi = mp.pi
ln2 = mp.log(2)

# Compute Li_2(1/2) and Li_3(1/2)
Li2_half = mp.polylog(2, 0.5)
Li3_half = mp.polylog(3, 0.5)

# Break down the expression into manageable terms
# Term 1: π³ / 48
term1 = pi**3 / 48

# Term 2: (π * (ln2)²) / 8
term2 = (pi * ln2**2) / 8

# Term 3: -(ln2 * Li₂(1/2)) / 4
term3 = -(ln2 * Li2_half) / 4

# Term 4: Li₃(1/2) / 8
term4 = Li3_half / 8

# Sum all terms to get final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))