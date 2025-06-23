import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Compute π²
pi_squared = mp.pi ** 2

# Compute ln(2)
ln_2 = mp.log(2)

# Compute first term: -2ζ(3)
term1 = -2 * zeta_3

# Compute second term: (π²/3) * ln(2)
term2 = (pi_squared / 3) * ln_2

# Sum the terms to get final result
result = term1 + term2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))