import mpmath as mp

# Set internal precision
mp.dps = 15

# Compute the gamma function values
gamma_3_4 = mp.gamma(3/4)
gamma_5_4 = mp.gamma(5/4)

# Compute the constant factor: sqrt(pi) * gamma(3/4) / (96 * gamma(5/4))
const_factor = (mp.sqrt(mp.pi) * gamma_3_4) / (96 * gamma_5_4)

# Compute the hypergeometric function: _2F_1(1/2, 3/4; 5/4; 1/16)
hyp_val = mp.hyp2f1(0.5, 0.75, 1.25, 1/16)

# Compute the first term: constant_factor * hyp_val
term1 = const_factor * hyp_val

# Compute the second term: (1/48) * arcsin(1/4)
term2 = (1/48) * mp.asin(0.25)

# Combine the terms: term1 - term2
result = term1 - term2

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))