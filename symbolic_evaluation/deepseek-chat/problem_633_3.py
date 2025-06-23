import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi squared
pi_squared = mp.pi**2

# Compute natural logarithm of 2
ln2 = mp.log(2)

# First term: - (pi^2 / 8) * ln(2)
term1 = - (pi_squared / 8) * ln2

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Second term: (7/16) * zeta(3)
term2 = (7/16) * zeta3

# Sum both terms
result = term1 + term2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))