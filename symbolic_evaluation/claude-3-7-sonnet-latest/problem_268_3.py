import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi = mp.pi

# Calculate ln(2)
ln2 = mp.log(2)

# Calculate zeta(3)
zeta3 = mp.zeta(3)

# Compute term1: (3 * pi^3 / 8) * ln(2)
pi_cubed = pi**3
term1 = (3 * pi_cubed / 8) * ln2

# Compute term2: pi^3 / 16
term2 = pi_cubed / 16

# Compute term3: (3 * pi / 8) * zeta(3)
term3 = (3 * pi / 8) * zeta3

# Combine terms: term1 - term2 - term3
result = term1 - term2 - term3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))