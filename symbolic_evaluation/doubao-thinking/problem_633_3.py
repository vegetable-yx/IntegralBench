import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Compute first term: (7/16) * ζ(3)
term1 = mp.fmul(7/16, zeta_3)

# Calculate components for second term
pi_squared = mp.power(mp.pi, 2)
ln2 = mp.log(2)

# Compute second term: (π²/8) * ln(2)
term2 = mp.fmul(mp.fdiv(pi_squared, 8), ln2)

# Combine terms for final result
result = term1 - term2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))