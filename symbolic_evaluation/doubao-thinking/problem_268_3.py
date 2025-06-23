import mpmath as mp
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply π and ζ(3)
pi_times_zeta3 = pi_value * zeta_3

# Divide by 8 to get final result
result = pi_times_zeta3 / 8

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))