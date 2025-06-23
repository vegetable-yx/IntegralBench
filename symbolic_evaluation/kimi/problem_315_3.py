import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute term: -(π²/4) * ln(2)
term1 = - (pi_squared / 4) * ln2

# Compute Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute term: (5/4) * ζ(3)
term2 = (5 / 4) * zeta3

# Sum both terms
result = term1 + term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))