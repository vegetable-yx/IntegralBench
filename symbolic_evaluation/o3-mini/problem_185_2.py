import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute constant sqrt(8)
sqrt8 = mp.sqrt(8)

# Calculate the two parameters for the gamma functions and hypergeometric function
a = (3 + sqrt8) / 4
b = (5 + sqrt8) / 4

# Compute the gamma function values
gamma_a = mp.gamma(a)
gamma_b = mp.gamma(b)

# Calculate the ratio of gamma functions
gamma_ratio = gamma_a / gamma_b

# Compute the hypergeometric function _2F1(1/2, a, b; -1)
hyp_val = mp.hyp2f1(0.5, a, b, -1)

# Calculate the constant factor: sqrt(pi)/4
constant_factor = mp.sqrt(mp.pi) / 4

# Combine all parts to get the final result
result = constant_factor * gamma_ratio * hyp_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))