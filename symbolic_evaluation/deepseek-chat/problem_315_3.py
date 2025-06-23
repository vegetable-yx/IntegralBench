import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π²/6
pi_squared_over_six = mp.pi**2 / 6

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Calculate (7/4) * ζ(3)
seven_fourths_zeta3 = (7 * zeta_3) / 4

# Compute the final result: π²/6 - (7/4)ζ(3)
result = pi_squared_over_six - seven_fourths_zeta3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))