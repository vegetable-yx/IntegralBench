import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Compute zeta(3) - Riemann zeta function at 3
zeta3 = mp.zeta(3)

# Compute natural logarithm of 2
log2 = mp.log(2)

# Calculate first term: - (47 * pi) / 32 * zeta(3)
term1 = - (47 * pi_val / 32) * zeta3

# Calculate second term: (pi^3 / 4) * log(2)
pi_cubed = pi_val ** 3
term2 = (pi_cubed / 4) * log2

# Sum both terms to get final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))