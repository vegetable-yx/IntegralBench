import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by π
pi_times_zeta3 = mp.pi * zeta_3

# Divide by 8 to get final result
result = pi_times_zeta3 / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))