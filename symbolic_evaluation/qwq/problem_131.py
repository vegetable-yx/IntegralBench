import mpmath as mp
mp.dps = 15

# Calculate the hypergeometric function 1F3(3/2; 1,1,2; 1/4)
a_param = mp.mpf('3/2')
b_params = (1, 1, 2)
z_value = mp.mpf('1/4')
hyper_result = mp.hyp1f3(a_param, b_params[0], b_params[1], b_params[2], z_value)

# Calculate the square root term sqrt(2*pi)
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Combine components for final result
result = sqrt_2pi * hyper_result

print(mp.nstr(result, n=10))