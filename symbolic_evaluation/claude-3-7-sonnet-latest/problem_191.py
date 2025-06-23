import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π (pi)
pi = mp.pi

# Compute ln(2)
ln2 = mp.log(2)

# Compute ln(1 + √2)
ln_term = mp.log(1 + mp.sqrt(2))

# Compute ζ(3) (Riemann zeta function at 3)
zeta3 = mp.zeta(3)

# Compute each term in the expression
term1 = pi**3 / 192
term2 = (pi / 16) * (ln2 ** 2)
term3 = -(pi / 4) * (ln_term ** 2)
term4 = (pi / 8) * zeta3

# Sum all terms to get the final result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))