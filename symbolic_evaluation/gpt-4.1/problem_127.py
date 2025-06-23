import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate gamma(1/4)
gamma_1_4 = mp.gamma(mp.mpf(1)/4)

# Calculate gamma(3/4)
gamma_3_4 = mp.gamma(mp.mpf(3)/4)

# Calculate the product of the gamma functions
gamma_product = gamma_1_4 * gamma_3_4

# Calculate the confluent hypergeometric function 1F1(11/4, 1, 1/2)
hyp_val = mp.hyp1f1(mp.mpf(11)/4, 1, mp.mpf(1)/2)

# Compute the final result
result = gamma_product * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))