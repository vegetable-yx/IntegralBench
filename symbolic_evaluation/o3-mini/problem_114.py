import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate pi^(3/2)
pi_power = mp.pi ** (3/2)

# Calculate Gamma(3/4) and then square it
gamma_val = mp.gamma(3/4)
gamma_sq = gamma_val ** 2

# Compute the denominator: 16 * [Gamma(3/4)]^2
denominator = 16 * gamma_sq

# Compute digamma function values: ψ(1/4) and ψ(3/4)
psi_1_4 = mp.digamma(1/4)
psi_3_4 = mp.digamma(3/4)

# Compute 2 * ln(2)
two_ln2 = 2 * mp.log(2)

# Combine the terms in the parentheses: ψ(1/4) - ψ(3/4) + 2*ln(2)
parentheses_term = psi_1_4 - psi_3_4 + two_ln2

# Combine all parts: numerator is pi_power * parentheses_term
numerator = pi_power * parentheses_term

# Final result: -(numerator / denominator)
result = -numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))