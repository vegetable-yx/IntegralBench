import mpmath as mp

mp.dps = 15  # Set internal decimal places for high precision

# Define the parameters for the hypergeometric function
a_params = [mp.mpf('0.5'), mp.mpf('0.5'), mp.mpf(1)]
b_params = [mp.mpf(1), mp.mpf(1), mp.mpf('1.5'), mp.mpf('1.5')]
z = mp.mpf(-1)

# Compute the hypergeometric function 3F4
hyper_result = mp.hyper(a_params, b_params, z)

# Multiply by pi/4 to get the final result
result = (mp.pi / 4) * hyper_result

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))