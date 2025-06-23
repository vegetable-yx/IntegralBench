import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute fundamental constants
ln2 = mp.log(2)
pi_sq = mp.pi**2
zeta3 = mp.zeta(3)

# Evaluate polylogarithms at 1/2
Li2_half = mp.polylog(2, 0.5)
Li3_half = mp.polylog(3, 0.5)

# Break expression into components
term1 = -ln2 * Li2_half
term2 = -0.5 * Li3_half
term3 = 0.5 * (ln2**3)
term4 = (pi_sq * ln2) / 8
term5 = -7 * zeta3 / 8

# Sum all terms
result = term1 + term2 + term3 + term4 + term5

# Print final value to 10 decimal places
print(mp.nstr(result, n=10))