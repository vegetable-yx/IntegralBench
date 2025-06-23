import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate zeta(3) - Apéry's constant
zeta_3 = mp.zeta(3)

# Multiply by pi
pi_times_zeta3 = mp.pi * zeta_3

# Divide by 8 to get the final result
result = pi_times_zeta3 / 8

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))