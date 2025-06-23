import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute intermediate constants
pi = mp.pi
pi_sq = pi**2
ln2 = mp.log(2)
zeta3 = mp.zeta(3)

# Break expression into manageable parts
term1 = 7 * pi_sq / 48
term2 = 7 * ln2**2 / 6
term3 = -pi_sq * ln2 / 8
term4 = -7 * zeta3 / 8
term5 = pi_sq / 16

# Combine terms for final result
result = term1 + term2 + term3 + term4 + term5

# Print result to 10 decimal places
print(mp.nstr(result, n=10))