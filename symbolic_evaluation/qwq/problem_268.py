import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply by 11
numerator = 11 * zeta_3

# Multiply by pi
product = mp.pi * numerator

# Divide by 16 to get final result
result = product / 16

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))