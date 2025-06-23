import mpmath as mp
mp.dps = 15

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute first term: -(π² * ln2)/6
term1 = -(pi_squared * ln2) / 6

# Compute ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute second term: -ζ(3)/8
term2 = -zeta_3 / 8

# Combine both terms for final result
result = term1 + term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))