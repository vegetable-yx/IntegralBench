import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the first term: -π²/6 * ln(2)
pi_squared = mp.pi**2
denominator = 6
ln2 = mp.log(2)
term1 = - (pi_squared / denominator) * ln2

# Compute the second term: (5/4) * ζ(3) where ζ is the Riemann zeta function
zeta3 = mp.zeta(3)
term2 = (5 / 4) * zeta3

# Sum the terms
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))