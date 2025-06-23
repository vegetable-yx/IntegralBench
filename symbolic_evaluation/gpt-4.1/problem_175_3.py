import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute each term of the analytical expression
# Term 1: pi^3 / 48
term1 = mp.pi**3 / 48

# Term 2: -(pi/4) * (ln(2))^2
ln2 = mp.ln(2)
term2 = -(mp.pi / 4) * ln2**2

# Term 3: -(pi/2) * dilogarithm(1/4)
dilog = mp.polylog(2, 1/mp.mpf(4))
term3 = -(mp.pi / 2) * dilog

# Term 4: (3*pi/16) * zeta(3)
zeta3 = mp.zeta(3)
term4 = (3 * mp.pi / 16) * zeta3

# Sum all terms to get the integral result
result = term1 + term2 + term3 + term4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))