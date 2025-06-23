import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate π
pi_val = mp.pi

# Compute term1: π³/48
pi_cubed = pi_val ** 3
term1 = pi_cubed / 48

# Compute term2: (π/8) * ln²(2)
ln2 = mp.log(2)
ln2_squared = ln2 ** 2
term2 = (pi_val / 8) * ln2_squared

# Compute term3: (1/4) * ζ(3)
zeta3 = mp.zeta(3)
term3 = zeta3 / 4

# Combine terms: π³/48 - (π/8)ln²(2) + (1/4)ζ(3)
result = term1 - term2 + term3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))