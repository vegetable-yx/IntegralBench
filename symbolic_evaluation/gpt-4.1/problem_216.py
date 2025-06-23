import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute Gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Compute Gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Compute the product of the Gamma functions
gamma_product = gamma_3_4 * gamma_1_4

# Compute the hypergeometric function 1F2 with parameters:
# a = 3/8, b1 = 1/2, b2 = 1/2, at z = -1
hyp = mp.hyper([mp.mpf(3)/8], [mp.mpf(1)/2, mp.mpf(1)/2], -1)

# Multiply the Gamma product with the hypergeometric function result
result = gamma_product * hyp

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))