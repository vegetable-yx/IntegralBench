import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute gamma function values
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)

# Calculate constant factor: sqrt(pi) * gamma(3/4)^2 / (32 * gamma(5/4))
sqrt_pi = mp.sqrt(mp.pi)
numerator_const = sqrt_pi * gamma_3_4**2
denominator_const = 32 * gamma_5_4
const_factor = numerator_const / denominator_const

# Compute hypergeometric function _3F_2([1/2, 1/2, 1], [3/2, 3/2]; 1/4)
a_list = [mp.mpf(1)/2, mp.mpf(1)/2, 1]
b_list = [mp.mpf(3)/2, mp.mpf(3)/2]
z_val = mp.mpf(1)/4
hyper_val = mp.hyper(a_list, b_list, z_val)

# Multiply constant factor by hypergeometric value
result = const_factor * hyper_val

# Print result to exactly 10 decimal places
print(mp.nstr(result, n=10))