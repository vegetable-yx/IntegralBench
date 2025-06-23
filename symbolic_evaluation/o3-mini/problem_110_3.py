import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute gamma function values
gamma_3_4 = mp.gamma(3/4)
gamma_5_4 = mp.gamma(5/4)

# Compute hypergeometric functions
hyp1 = mp.hyp2f1(-0.5, 0.25, 0.75, 1/16)  # 2F1(-1/2, 1/4; 3/4; 1/16)
hyp2 = mp.hyp2f1(0.5, 0.25, 1.25, 1/16)    # 2F1(1/2, 1/4; 5/4; 1/16)

# Compute the bracket expression: 8 * hyp1 - hyp2
bracket_expr = 8 * hyp1 - hyp2

# Compute the coefficient: π^(3/2) * Γ(3/4) / (16 * Γ(5/4))
pi_term = mp.pi ** 1.5
numerator = pi_term * gamma_3_4
denominator = 16 * gamma_5_4
coeff = numerator / denominator

# Multiply coefficient by bracket expression
result = coeff * bracket_expr

# Print result to 10 decimal places
print(mp.nstr(result, n=10))