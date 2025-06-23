import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute the Riemann zeta function at 3 (Apéry's constant)
zeta_3 = mp.zeta(3)

# Multiply by the rational factor 7/8
factor = mp.mpf(7)/8
result = factor * zeta_3

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))