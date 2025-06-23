import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute each term separately for clarity and error avoidance

# Calculate ζ(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Calculate ζ(3, 3/2) - Hurwitz zeta function with parameters s=3, a=3/2
zeta3_32 = mp.zeta(3, mp.mpf('3/2'))

# Calculate ζ(3, 3/4) - Hurwitz zeta function with parameters s=3, a=3/4
zeta3_34 = mp.zeta(3, mp.mpf('3/4'))

# Calculate ζ(3, 5/4) - Hurwitz zeta function with parameters s=3, a=5/4
zeta3_54 = mp.zeta(3, mp.mpf('5/4'))

# Combine terms according to the expression: 56ζ(3) - 8ζ(3, 3/2) - ζ(3, 3/4) + ζ(3, 5/4)
result = 56 * zeta3 - 8 * zeta3_32 - zeta3_34 + zeta3_54

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))