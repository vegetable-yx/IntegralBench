import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by the constant fraction 7/8
result = mp.fmul(zeta_3, mp.mpf(7)/8)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))