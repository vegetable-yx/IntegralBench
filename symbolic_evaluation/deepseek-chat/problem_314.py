import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute the first term: (7/8) * zeta(3)
term1 = (mp.mpf(7)/8) * zeta3

# Compute pi squared
pi_squared = mp.pi ** 2

# Compute natural logarithm of 2
ln2 = mp.log(2)

# Compute the second term: (pi^2 / 4) * ln(2)
term2 = (pi_squared / 4) * ln2

# Subtract the second term from the first
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))