import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate Gamma(3/4)
gamma_3_4 = mp.gamma(3/4)

# Calculate Gamma(5/4)
gamma_5_4 = mp.gamma(5/4)

# Compute the constant factor: (sqrt(2) * Gamma(3/4)) / (2 * Gamma(5/4))
numerator = mp.sqrt(2) * gamma_3_4
denominator = 2 * gamma_5_4
constant_factor = numerator / denominator

# Calculate the hypergeometric function _0F_1(; 3/4; 1/8)
hyper_term = mp.hyp0f1(3/4, 1/8)

# Multiply constant factor by hypergeometric term to get final result
result = constant_factor * hyper_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))