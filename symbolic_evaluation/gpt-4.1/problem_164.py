import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute π^4
pi_4 = mp.pi**4

# Calculate the first term: (8 * π^4) / 15
term1 = (8 * pi_4) / 15

# Compute Hurwitz zeta functions: ζ(4, 0.75) and ζ(4, 1.25)
zeta_4_075 = mp.zeta(4, 0.75)
zeta_4_125 = mp.zeta(4, 1.25)

# Calculate the sum of the two zeta values
zeta_sum = zeta_4_075 + zeta_4_125

# Multiply the zeta sum by 3
term2 = 3 * zeta_sum

# Combine terms: first term minus second term
result = term1 - term2

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))