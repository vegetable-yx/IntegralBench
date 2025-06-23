import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute each Hurwitz zeta term separately
# ζ(3, 0.5)
term1 = 8 * mp.zeta(3, 0.5)

# ζ(3, 1.5)
term2 = 8 * mp.zeta(3, 1.5)

# ζ(3, 0.75)
term3 = mp.zeta(3, 0.75)

# ζ(3, 1.25)
term4 = mp.zeta(3, 1.25)

# Combine terms according to the expression: 8ζ(3,0.5) - 8ζ(3,1.5) - ζ(3,0.75) + ζ(3,1.25)
result = term1 - term2 - term3 + term4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))