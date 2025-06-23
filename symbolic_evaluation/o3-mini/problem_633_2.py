import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π²
pi_sq = mp.pi**2

# Compute ln(2)
ln2 = mp.log(2)

# Compute the first term: -π²·ln(2)/8
term1 = -pi_sq * ln2 / 8

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute the second term: 7·ζ(3)/16
term2 = 7 * zeta3 / 16

# Sum both terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))