import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute fundamental constants
pi = mp.pi
ln2 = mp.log(2)

# Compute polylogarithms at x=1/2
Li2 = mp.polylog(2, 0.5)
Li3 = mp.polylog(3, 0.5)

# Break expression into terms
term1 = (pi**3 / 96) * ln2
term2 = (pi / 32) * (ln2**3)
term3 = (1/32) * Li3
term4 = (-1/64) * ln2 * Li2

# Sum all terms
result = term1 + term2 + term3 + term4

# Print final result to 10 decimal places
print(mp.nstr(result, n=10))