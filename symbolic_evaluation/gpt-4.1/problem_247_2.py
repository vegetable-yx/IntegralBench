import mpmath as mp

# Set decimal places for internal precision
mp.dps = 15

# Compute zeta(3) - Apéry's constant
zeta_3 = mp.zeta(3)

# Multiply zeta(3) by 7/2
term = (7/2) * zeta_3

# Add 1 to the term
numerator = 1 + term

# Divide by 16 to get the final result
result = numerator / 16

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))