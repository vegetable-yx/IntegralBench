import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute each component of the expression step by step
sqrt_pi = mp.sqrt(mp.pi)  # Square root of pi
gamma_1_4 = mp.gamma(mp.mpf(1)/4)  # Gamma(1/4)
gamma_1_4_squared = gamma_1_4 ** 2  # Gamma(1/4)^2
gamma_1_2 = mp.gamma(mp.mpf(1)/2)  # Gamma(1/2)
denominator = mp.sqrt(2) * gamma_1_2  # 2^(1/2) * Gamma(1/2)

# Combine the components for the first part of the expression
part1 = sqrt_pi * gamma_1_4_squared / denominator

# Compute the hypergeometric function {}_1F_2(1/4; 3/4, 1/2; -1/4)
hyper_term = mp.hyper([mp.mpf(1)/4], [mp.mpf(3)/4, mp.mpf(1)/2], -mp.mpf(1)/4)

# Multiply all parts to get the final result
result = part1 * hyper_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))