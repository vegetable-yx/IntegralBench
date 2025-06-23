import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Calculate 2^(5/4) using exact fractional exponent
two_power = mp.power(2, mp.mpf('5/4'))

# Compute square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate ratio of Gamma functions
gamma_ratio = mp.gamma(mp.mpf('1/4')) / mp.gamma(mp.mpf('3/4'))

# Parameters for hypergeometric function _1F2
a = mp.mpf('1/4')
b_params = (mp.mpf('3/4'), mp.mpf('1/2'))
z = mp.mpf('-1/4')

# Evaluate hypergeometric function
hyper_term = mp.hyp1f2(a, b_params, z)

# Combine all components for final result
result = two_power * sqrt_pi * gamma_ratio * hyper_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))