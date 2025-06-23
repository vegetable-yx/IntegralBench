import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Compute the natural logarithm of 2
ln2 = mp.ln(2)

# Compute the constant pi
pi = mp.pi

# Calculate the first term: (7 * pi * zeta(3)) / 16
term1 = (7 * pi * zeta_3) / 16

# Calculate the second term: (pi^3 * ln(2)) / 24
term2 = (pi**3 * ln2) / 24

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))