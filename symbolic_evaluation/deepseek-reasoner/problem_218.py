import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute ln(2) once for reuse
ln2 = mp.log(2)

# Calculate each term of the expression separately
term1 = (mp.pi / 3) * (ln2 ** 2)          # π/3 (ln2)^2
term2 = (mp.pi ** 3) / 72                 # π³/72
term3 = -(mp.pi / 3) * (ln2 ** 3)         # -π/3 (ln2)^3
term4 = -ln2 * mp.clsin(2, mp.pi/3)       # -ln2 * Cl₂(π/3)
term5 = -0.5 * mp.clsin(3, mp.pi/3)       # -1/2 Cl₃(π/3)

# Sum all terms to get final result
result = term1 + term2 + term3 + term4 + term5

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))