import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute constants and gamma functions
pi = mp.pi
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Compute the coefficient: pi^(3/2) * [gamma(3/4)]^2 / {16 * [gamma(5/4)]^2}
pi_power = mp.power(pi, mp.mpf(3)/2)
gamma_ratio_sq = mp.power(gamma_3_4, 2) / mp.power(gamma_5_4, 2)
coeff = pi_power * gamma_ratio_sq / 16

# Compute the hypergeometric functions
hyp1 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/2, mp.mpf(3)/4, mp.mpf(1)/4)
hyp2 = mp.hyp2f1(mp.mpf(-1)/2, mp.mpf(1)/2, mp.mpf(5)/4, mp.mpf(1)/4)

# Combine the hypergeometric part: hyp1 - 2 * hyp2
hyper_part = hyp1 - 2 * hyp2

# Multiply coefficient by hypergeometric part to get final result
result = coeff * hyper_part

# Print result to 10 decimal places
print(mp.nstr(result, n=10))