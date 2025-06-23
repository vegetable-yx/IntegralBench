import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the first Hurwitz zeta function term ζ(3, 3/4)
zeta_term1 = mp.zeta(3, 3/4)

# Compute the second Hurwitz zeta function term ζ(3, 5/4)
zeta_term2 = mp.zeta(3, 5/4)

# Combine all terms according to the expression: 64 - ζ(3, 3/4) + ζ(3, 5/4)
result = 64 - zeta_term1 + zeta_term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))