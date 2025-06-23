import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π squared
pi_sq = mp.pi ** 2

# Compute ln(2)
ln2 = mp.log(2)

# First term: -(π²/8) * ln(2)
term1 = - (pi_sq / 8) * ln2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Second term: (7/16) * ζ(3)
term2 = (7 / 16) * zeta3

# Sum both terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))