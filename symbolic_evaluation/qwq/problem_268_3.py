import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi_val = mp.pi

# Calculate ζ(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply π and ζ(3)
product = pi_val * zeta_3

# Divide by 8 to get final result
result = product / 8

# Print result with 10 decimal places
print(mp.nstr(result, n=10))