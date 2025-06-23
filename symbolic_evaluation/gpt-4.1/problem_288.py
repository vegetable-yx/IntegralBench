import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Compute the Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Calculate the constant factor: pi/8
pi_over_8 = pi_val / 8

# Multiply by zeta(3) to get the final result
result = pi_over_8 * zeta_3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))