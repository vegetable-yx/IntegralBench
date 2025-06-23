import mpmath as mp
mp.dps = 15

# Calculate ζ(3) using Riemann zeta function
zeta_3 = mp.zeta(3)

# Multiply by π
pi_times_zeta3 = mp.pi * zeta_3

# Divide by 8 to get final result
result = pi_times_zeta3 / 8

print(mp.nstr(result, n=10))