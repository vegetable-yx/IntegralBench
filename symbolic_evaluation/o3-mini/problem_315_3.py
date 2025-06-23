import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate ln(2) once for reuse
ln2 = mp.log(2)

# Compute term1: π² * ln(2) / 4
pi_sq = mp.pi ** 2
term1 = (pi_sq * ln2) / 4

# Compute term2: ln(2) * Li₂(1/2)
li2_half = mp.polylog(2, 0.5)
term2 = ln2 * li2_half

# Compute term3: -(2/3) * (ln2)^3
ln2_cubed = ln2 ** 3
term3 = - (mp.mpf(2)/3) * ln2_cubed

# Compute term4: (3/2) * ζ(3)
zeta3 = mp.zeta(3)
term4 = (mp.mpf(3)/2) * zeta3

# Sum all terms
result = term1 + term2 + term3 + term4

# Print result to 10 decimal places
print(mp.nstr(result, n=10))