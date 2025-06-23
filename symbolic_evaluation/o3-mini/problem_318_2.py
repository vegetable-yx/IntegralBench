import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Define the value of a (assuming a is provided; here we set a=1 as an example)
a = mp.mpf(1)

# Calculate common constants and gamma functions
sqrt_pi = mp.sqrt(mp.pi)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)
gamma_5_4 = mp.gamma(mp.mpf(5)/4)
gamma_7_4 = mp.gamma(mp.mpf(7)/4)

# Precompute the argument for the hypergeometric functions
arg = -a**2 / 4

# Calculate the first term components
factor1_num = sqrt_pi * gamma_3_4
factor1_den = 2 * gamma_5_4
factor1 = factor1_num / factor1_den
hyper1 = mp.hyper([mp.mpf(1)/4], [mp.mpf(1)/2, mp.mpf(5)/4], arg)
term1 = factor1 * hyper1

# Calculate the second term components
factor2_num = a**2 * sqrt_pi * gamma_3_4
factor2_den = 6 * gamma_7_4
factor2 = factor2_num / factor2_den
hyper2 = mp.hyper([mp.mpf(3)/4], [mp.mpf(3)/2, mp.mpf(7)/4], arg)
term2 = factor2 * hyper2

# Combine the terms to get the result
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))