import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π
pi = mp.pi

# Calculate ln(2)
ln2 = mp.log(2)

# First term: (π * ln(2)) / 2
term1 = (pi * ln2) / 2

# Compute ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Second term: (7/8) * ζ(3)
term2 = (mp.mpf(7)/8) * zeta3

# Combine terms: result = term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))