import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute the hypergeometric function: {}_3F_2(1, 1, 3/2; 2, 3; 1)
# Using mp.hyper with parameters: [a1, a2, a3], [b1, b2], z
hyper_val = mp.hyper([1, 1, mp.mpf(3)/2], [2, 3], 1)

# Multiply the hypergeometric result by 1/32
result = hyper_val / 32

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))