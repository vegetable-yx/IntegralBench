import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Compute the first term: (7/16) * ζ(3)
zeta_3 = mp.zeta(3)
term1 = (7/16) * zeta_3

# Compute the second term: (π²/8) * ln(2)
pi_squared = mp.pi ** 2
ln2 = mp.log(2)
term2 = (pi_squared * ln2) / 8

# Combine the terms
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))