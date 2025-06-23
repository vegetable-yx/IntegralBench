import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Compute constants and gamma functions
pi_power = mp.power(mp.pi, 1.5)  # pi^(3/2)
gamma1 = mp.gamma(1/4)  # Gamma(1/4)
gamma2 = mp.gamma(3/4)  # Gamma(3/4)

# Calculate the coefficient: 3 * pi^(3/2) * Gamma(1/4) / (16 * Gamma(3/4))
numerator = 3 * pi_power * gamma1
denominator = 16 * gamma2
coeff = numerator / denominator

# Compute the hypergeometric function: _2F_1(-1/2, 1/4; 3/4; 1/4)
hyp_val = mp.hyp2f1(-0.5, 0.25, 0.75, 0.25)

# Multiply coefficient by hypergeometric value
result = coeff * hyp_val

# Print result to 10 decimal places
print(mp.nstr(result, n=10))