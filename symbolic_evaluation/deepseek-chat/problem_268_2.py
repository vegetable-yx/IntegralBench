import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi_val = mp.pi

# Divide pi by 16
pi_over_16 = pi_val / 16

# Calculate zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply pi/16 by zeta(3) and negate the result
result = -pi_over_16 * zeta_3

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))