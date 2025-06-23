import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Compute pi squared
pi_sq = mp.pi ** 2

# Calculate Gamma(3/4) and square it
gamma_34 = mp.gamma(3/4)
gamma_34_sq = gamma_34 ** 2

# Calculate Gamma(5/4) and square it
gamma_54 = mp.gamma(5/4)
gamma_54_sq = gamma_54 ** 2

# Compute the numerator: pi^2 * [Gamma(3/4)]^2
numerator = pi_sq * gamma_34_sq

# Compute the denominator: 64 * [Gamma(5/4)]^2
denominator = 64 * gamma_54_sq

# Calculate the fraction: numerator / denominator
fraction = numerator / denominator

# Compute the hypergeometric function 2F1(-3/2, 1/2; 1; 1/2)
hyp_val = mp.hyp2f1(-3/2, 1/2, 1, 1/2)

# Multiply the fraction by the hypergeometric value to get the result
result = fraction * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))