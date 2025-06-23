import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the parameters for the hypergeometric function _4F_3
# Numerator parameters: four instances of 1/2
a_params = [mp.mpf(1)/2] * 4
# Denominator parameters: [3, 1, 1]
b_params = [3, 1, 1]
# Argument z = 1
z_val = 1

# Compute the hypergeometric function value
hyper_val = mp.hyper(a_params, b_params, z_val)

# Calculate the constant factor: π²/12
pi_sq = mp.pi ** 2
constant_factor = pi_sq / 12

# Compute the final result
result = constant_factor * hyper_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))