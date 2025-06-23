import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma functions and constants
gamma_1_4 = mp.gamma(0.25)  # Γ(1/4)
gamma_3_4 = mp.gamma(0.75)  # Γ(3/4)
sqrt2 = mp.sqrt(2)          # √2
pi_sqrt = mp.sqrt(mp.pi)    # √π
pi_3_2 = mp.pi * pi_sqrt    # π^(3/2)

# Compute first term: √2 * π^(3/2) * Γ(1/4) / [16 * Γ(3/4)]
numerator1 = sqrt2 * pi_3_2 * gamma_1_4
denominator1 = 16 * gamma_3_4
term1 = numerator1 / denominator1

# Compute second term: [Γ(1/4)^2 / 8] * _2F_1(1/4, 1/2; 3/4; 1/2)
gamma_sq = gamma_1_4 ** 2  # Γ(1/4)^2
denominator2 = 8
# Hypergeometric function _2F_1(1/4, 1/2; 3/4; 1/2)
hyp_val = mp.hyp2f1(0.25, 0.5, 0.75, 0.5)
term2 = (gamma_sq / denominator2) * hyp_val

# Final result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))