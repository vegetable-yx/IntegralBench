import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply ζ(3) by π
pi_times_zeta3 = mp.pi * zeta_3

# Divide by 4 and negate to get final result
result = -pi_times_zeta3 / 4

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))