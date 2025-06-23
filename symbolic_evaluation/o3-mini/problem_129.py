import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute Gamma(3/4)
gamma_val = mp.gamma(mp.mpf(3)/4)

# Square Gamma(3/4)
gamma_sq = gamma_val ** 2

# Compute 2^(1/4)
two_power = mp.power(2, mp.mpf(1)/4)

# Compute the numerator: Gamma(3/4)^2 * 2^(1/4)
numerator = gamma_sq * two_power

# Compute the denominator: 2 * sqrt(pi)
denominator = 2 * mp.sqrt(mp.pi)

# Compute the hypergeometric function _1F_2(1/4; 1/2, 3/4; 1/64)
hyp = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(3)/4], mp.mpf(1)/64)

# Combine the parts: (numerator / denominator) * hyp
result = (numerator / denominator) * hyp

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))