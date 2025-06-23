import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define common arguments for the hypergeometric functions
a1 = mp.mpf(1)/2
a2 = a1  # a2 = 1/2
a3_first = mp.mpf(3)/2  # 3/2 for the first hypergeometric
a3_second = a1  # 1/2 for the second hypergeometric
b1 = mp.mpf(3)/4
b2 = mp.mpf(5)/4
z_arg = mp.mpf(1)/16  # 1/16

# Compute the first hypergeometric function: _3F_2(1/2, 1/2, 3/2; 3/4, 5/4; 1/16)
hyper1 = mp.hyper3f2(a1, a2, a3_first, b1, b2, z_arg)

# Compute the second hypergeometric function: _3F_2(1/2, 1/2, 1/2; 3/4, 5/4; 1/16)
hyper2 = mp.hyper3f2(a1, a2, a3_second, b1, b2, z_arg)

# Calculate the first term: (π/16) * hyper1
term1 = (mp.pi / 16) * hyper1

# Calculate the second term: (1/4) * hyper2
term2 = (mp.mpf(1)/4) * hyper2

# Combine the results: term1 - term2
result = term1 - term2

# Print the final result with 10 decimal places
print(mp.nstr(result, n=10))