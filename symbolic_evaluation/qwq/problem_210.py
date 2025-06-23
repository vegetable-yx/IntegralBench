import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi * ln(2) component
pi_term = mp.pi
ln2 = mp.log(2)
term1 = pi_term * ln2

# Calculate 4 * Dirichlet beta function at 3
beta3 = mp.dirichletbeta(3)
term2 = 4 * beta3

# Combine both terms for final result
result = term1 + term2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))