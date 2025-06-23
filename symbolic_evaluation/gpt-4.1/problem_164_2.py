import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the first term: 48 * ζ(4, 1.5)
term1 = 48 * mp.zeta(4, 1.5)

# Calculate ζ(4, 1.25)
zeta_4_125 = mp.zeta(4, 1.25)

# Calculate ζ(4, 1.75)
zeta_4_175 = mp.zeta(4, 1.75)

# Combine the second term: 3 * [ζ(4, 1.25) + ζ(4, 1.75)]
term2 = 3 * (zeta_4_125 + zeta_4_175)

# Final result: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))