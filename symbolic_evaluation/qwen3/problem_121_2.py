import mpmath as mp
mp.dps = 15

# Calculate the 4F3 hypergeometric function with parameters (1/2,1/2,1/2,1/2; 1,1,1; 1)
a_params = [0.5, 0.5, 0.5, 0.5]
b_params = [1, 1, 1]
hypergeometric_value = mp.hyper(a_params, b_params, 1)

# Calculate π²/4 term
pi_squared_over_4 = (mp.pi ** 2) / 4

# Compute final result by multiplying components
result = pi_squared_over_4 * hypergeometric_value

print(mp.nstr(result, n=10))