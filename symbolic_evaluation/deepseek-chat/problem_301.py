import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate fundamental constants
pi_sq = mp.pi**2       # π²
ln2 = mp.log(2)        # Natural logarithm of 2
zeta3 = mp.zeta(3)     # Riemann zeta function at 3

# Compute each term of the expression
term1 = pi_sq / 6                  # π²/6
term2 = 2 * (ln2)**2               # 2 ln²2
term3 = (pi_sq / 12) * ln2         # (π²/12) ln2
term4 = (mp.mpf(7)/4) * zeta3     # (7/4) ζ(3)

# Combine terms: π²/6 - 2ln²2 - (π²/12)ln2 + (7/4)ζ(3)
result = term1 - term2 - term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))