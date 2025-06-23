import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant factor: sqrt(pi) * Gamma(3/4) / (8 * Gamma(5/4))
sqrt_pi = mp.sqrt(mp.pi)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)
constant_factor = (sqrt_pi * gamma_3_4) / (8 * gamma_5_4)

# Compute the hypergeometric function _1F_2(1/2; 3/4, 5/4; -1/4)
a_list = [mp.mpf(1)/2]  # numerator parameters
b_list = [mp.mpf(3)/4, mp.mpf(5)/4]  # denominator parameters
z_val = mp.mpf(-1)/4
hyp_val = mp.hyper(a_list, b_list, z_val)

# Multiply constant factor by hypergeometric result
product = constant_factor * hyp_val

# Subtract the term pi/8
pi_term = mp.pi / 8
result = product - pi_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))