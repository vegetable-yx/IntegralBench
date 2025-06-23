import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute pi cubed
pi_cubed = mp.pi ** 3

# Divide pi cubed by 8
first_term = pi_cubed / 8

# Compute zeta(3) - Riemann zeta function at 3
zeta_3 = mp.zeta(3)

# Multiply zeta(3) by 2
second_term = 2 * zeta_3

# Combine terms: π³/8 - 2ζ(3)
result = first_term - second_term

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))