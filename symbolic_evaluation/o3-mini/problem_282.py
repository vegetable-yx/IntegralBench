import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define input parameters (example values - user should modify these)
a = 1.0
b = 1.0

# Compute the argument for the hypergeometric function
z = (b**2 * a**2) / 16

# Calculate the gamma function term: Γ(1/4)
gamma_term = mp.gamma(0.25)  # 0.25 = 1/4

# Square the gamma term
gamma_sq = gamma_term**2

# Compute the denominator: sqrt(π)
denom = mp.sqrt(mp.pi)

# Combine gamma and denominator terms
gamma_denom_ratio = gamma_sq / denom

# Calculate the confluent hypergeometric function ₁F₁(1/4; 1/2; z)
hyp = mp.hyp1f1(0.25, 0.5, z)  # 0.25=1/4, 0.5=1/2

# Compute the a^{-1/2} term
a_power = a**(-0.5)  # -0.5 = -1/2

# Multiply all components together
result = a_power * gamma_denom_ratio * hyp

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))