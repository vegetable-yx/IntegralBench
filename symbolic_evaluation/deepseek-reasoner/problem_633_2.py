import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate ζ(3) using the Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute the first term: (7/16) * ζ(3)
term1 = (7/16) * zeta_3

# Calculate π²
pi_squared = mp.pi ** 2

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Compute the second term: (π²/8) * ln2
term2 = (pi_squared / 8) * ln2

# Combine terms to get final result
result = term1 - term2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))