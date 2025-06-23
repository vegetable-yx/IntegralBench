import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π²
pi_squared = mp.pi ** 2

# Compute π²/6
pi_sq_over_6 = pi_squared / 6

# Compute natural logarithm of 2
ln2 = mp.log(2)

# First term: (π²/6) * ln(2)
term1 = pi_sq_over_6 * ln2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Second term: (11/8) * ζ(3)
term2 = (11 * zeta3) / 8

# Final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))