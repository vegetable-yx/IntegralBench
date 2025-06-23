import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the numerator: sqrt(pi) * gamma(1/8)
numerator = mp.sqrt(mp.pi) * mp.gamma(1/8)

# Compute the denominator: 28 * gamma(5/8)
denominator = 28 * mp.gamma(5/8)

# Compute each digamma term in the bracket
psi_half = mp.digamma(1/2)
psi_one_eighth = mp.digamma(1/8)
psi_five_eighths = mp.digamma(5/8)
psi_one = mp.digamma(1)

# Combine terms: ψ(1/2) - ψ(1/8) - ψ(5/8) + 2*ψ(1)
bracket_term = psi_half - psi_one_eighth - psi_five_eighths + 2 * psi_one

# Multiply the fraction by the bracket term
result = (numerator / denominator) * bracket_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))