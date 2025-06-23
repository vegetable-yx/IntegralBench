import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the value of 'a' (can be modified as needed)
a = 1.0

# Calculate the common argument for hypergeometric functions
arg = -a**2 / 16

# Compute the first hypergeometric function: {}_1F_2(1/2; 3/4, 5/4; arg)
hyper1 = mp.hyper([mp.mpf(1)/2], [mp.mpf(3)/4, mp.mpf(5)/4], arg)

# First term: (π/2) * hyper1
term1 = (mp.pi / 2) * hyper1

# Compute gamma function values
gamma34 = mp.gamma(mp.mpf(3)/4)  # Γ(3/4)
gamma54 = mp.gamma(mp.mpf(5)/4)  # Γ(5/4)

# Calculate coefficient: a * Γ(3/4)^2 / (2√2 * Γ(5/4))
coeff = (a * gamma34**2) / (2 * mp.sqrt(2) * gamma54)

# Compute the second hypergeometric function: {}_1F_2(1; 3/4, 3/2; arg)
hyper2 = mp.hyper([1], [mp.mpf(3)/4, mp.mpf(3)/2], arg)

# Second term: coeff * hyper2
term2 = coeff * hyper2

# Combine terms for final result
result = term1 - term2

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))