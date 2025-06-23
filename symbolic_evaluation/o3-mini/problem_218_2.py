import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute fundamental constants and values
ln2 = mp.log(2)      # Natural logarithm of 2
pi = mp.pi           # Pi constant
pi_sq = pi**2        # Pi squared
ln2_sq = ln2**2      # (ln2)^2
ln2_cu = ln2**3      # (ln2)^3

# Calculate each term of the expression separately
term1 = (pi * ln2_sq) / 6
term2 = mp.zeta(3) / 8
term3 = (pi_sq * ln2) / 72
term4 = -ln2_cu / 24

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))