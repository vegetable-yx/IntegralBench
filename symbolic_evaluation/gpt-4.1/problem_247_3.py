import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant term: 1/16
constant_term = mp.mpf(1) / 16

# Calculate the coefficient for zeta(3): 7/32
zeta_coeff = mp.mpf(7) / 32

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Multiply coefficient by zeta(3)
zeta_term = zeta_coeff * zeta3

# Sum the constant term and the zeta term
result = constant_term + zeta_term

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))