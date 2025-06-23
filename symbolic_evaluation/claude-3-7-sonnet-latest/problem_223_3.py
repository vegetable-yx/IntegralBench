import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate zeta(3) - Apéry's constant
zeta_3 = mp.zeta(3)

# Multiply by 2*pi
result = 2 * mp.pi * zeta_3

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))