import mpmath as mp

mp.dps = 15  # Set internal precision

# Define parameters for the hypergeometric function
a_params = [mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf(1)]
b_params = [mp.mpf('1.5'), mp.mpf('1.5'), mp.mpf('1.5'), mp.mpf('1.5')]
z_value = mp.mpf(-1)

# Compute the hypergeometric function 3F4
hyper_result = mp.hyper(a_params, b_params, z_value)

# Multiply by π/8 to get final result
result = (mp.pi / 8) * hyper_result

# Print with 10 decimal precision
print(mp.nstr(result, n=10))