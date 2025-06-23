import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate ln(2) once for reuse
ln2 = mp.log(2)

# Calculate Li_2(1/2) and Li_3(1/2) using polylog function
Li2_half = mp.polylog(2, 0.5)
Li3_half = mp.polylog(3, 0.5)

# Compute each term of the expression
# Term1: (π/2) * (ln(2))^2
term1 = (mp.pi / 2) * (ln2 ** 2)

# Term2: 2 * ln(2) * Li_2(1/2)
term2 = 2 * ln2 * Li2_half

# Term3: -2 * Li_3(1/2)
term3 = -2 * Li3_half

# Sum all terms
result = term1 + term2 + term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))