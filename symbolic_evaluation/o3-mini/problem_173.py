import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi
pi = mp.pi

# Compute term1: \frac{\pi^3}{144}
term1 = (pi ** 3) / 144

# Compute the factor: \frac{\pi - 4}{16}
factor = (pi - 4) / 16

# Evaluate elliptic integrals at k = 1/2
E_half = mp.ellipe(0.5)  # E(1/2)
K_half = mp.ellipk(0.5)  # K(1/2)

# Compute the expression inside the brackets: 2*E(1/2) - K(1/2)
bracket_term = 2 * E_half - K_half

# Compute term2: factor multiplied by bracket_term
term2 = factor * bracket_term

# Sum both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))