import mpmath as mp
mp.dps = 15  # Set decimal precision for internal calculations

# Calculate ζ(3, 1/4) using Hurwitz zeta function
zeta_term1 = mp.zeta(3, 1/4)

# Calculate ζ(3, 3/4) using Hurwitz zeta function
zeta_term2 = mp.zeta(3, 3/4)

# Compute the difference between the two zeta values
result = zeta_term1 - zeta_term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))