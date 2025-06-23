import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Define constants and intermediate values
pi = mp.pi
ln2 = mp.log(2)
sqrt2 = mp.sqrt(2)
one_plus_sqrt2 = 1 + sqrt2
ln_one_plus_sqrt2 = mp.log(one_plus_sqrt2)

# Calculate each term of the expression
term1 = pi**4 / 360
term2 = -(pi**2 * ln2**2) / 24
term3 = ln2**4 / 24
term4 = (pi**2 * ln2 * ln_one_plus_sqrt2) / 12
term5 = -(ln2**3 * ln_one_plus_sqrt2) / 6
term6 = -(pi**2 * ln_one_plus_sqrt2**2) / 24
term7 = (ln2**2 * ln_one_plus_sqrt2**2) / 4
term8 = -(ln2 * ln_one_plus_sqrt2**3) / 6
term9 = ln_one_plus_sqrt2**4 / 24

# Sum all terms
result = term1 + term2 + term3 + term4 + term5 + term6 + term7 + term8 + term9

# Print result to 10 decimal places
print(mp.nstr(result, n=10))