import mpmath as mp

# Set decimal places for internal calculations
mp.dps = 15

# Compute Gamma(3/4)
gamma_34 = mp.gamma(3/4)

# Square Gamma(3/4)
gamma_34_sq = gamma_34**2

# Compute Gamma(5/4)
gamma_54 = mp.gamma(5/4)

# Compute the hypergeometric function 2F1(1/2, 3/4; 5/4; 1/4)
hyp_val = mp.hyp2f1(0.5, 0.75, 1.25, 0.25)

# Compute numerator: sqrt(pi) * [Gamma(3/4)]^2
numerator = mp.sqrt(mp.pi) * gamma_34_sq

# Compute denominator: 4 * Gamma(5/4)
denominator = 4 * gamma_54

# Combine: (numerator / denominator) * hypergeometric value
result = (numerator / denominator) * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))