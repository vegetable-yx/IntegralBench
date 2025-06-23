import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma function values
gamma_34 = mp.gamma(3/4)
gamma_54 = mp.gamma(5/4)

# Calculate the multiplicative factor: sqrt(2) * Gamma(3/4) / (4 * Gamma(5/4))
factor = (mp.sqrt(2) * gamma_34) / (4 * gamma_54)

# Calculate the ratio of gamma squares: 4 * [Gamma(5/4)]^2 / [Gamma(3/4)]^2
gamma_ratio = 4 * (gamma_54 ** 2) / (gamma_34 ** 2)

# Compute the first hypergeometric function: {}_{1}F_{2}(3/4; 1/2, 5/4; -1/64)
hyp1 = mp.hyper([3/4], [1/2, 5/4], -1/64)

# Compute the second hypergeometric function: {}_{1}F_{2}(5/4; 3/2, 7/4; -1/64)
hyp2 = mp.hyper([5/4], [3/2, 7/4], -1/64)

# Combine the hypergeometric terms: hyp1 - gamma_ratio * hyp2
hyper_comb = hyp1 - gamma_ratio * hyp2

# Multiply by the factor to get the final result
result = factor * hyper_comb

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))