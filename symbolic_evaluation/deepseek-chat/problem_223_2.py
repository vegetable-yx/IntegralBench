import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute zeta(3) using mpmath's zeta function
zeta_3 = mp.zeta(3)

# Multiply by the rational coefficient 7/4
result = mp.fmul(zeta_3, mp.mpf(7)/4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))