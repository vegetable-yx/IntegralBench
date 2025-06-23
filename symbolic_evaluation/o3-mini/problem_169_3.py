import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the first generalized hypergeometric function
# {}_3F_2(1/2, 1/2, 1/2; 1, 3/2; 1/16)
hyper1 = mp.hyper([0.5, 0.5, 0.5], [1, 1.5], 1/16)

# Compute the second generalized hypergeometric function
# {}_3F_2(1/2, 1/2, 1/2; 1, 3/2; 1/4)
hyper2 = mp.hyper([0.5, 0.5, 0.5], [1, 1.5], 0.25)

# Compute the argument for the logarithm: (sqrt(2) + 1) / (sqrt(2) - 1)
sqrt2 = mp.sqrt(2)
log_arg = (sqrt2 + 1) / (sqrt2 - 1)

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute the first term: (π/4) * hyper1
term1 = (mp.pi / 4) * hyper1

# Compute the second term: (1/8) * log_val * hyper2
term2 = (1/8) * log_val * hyper2

# Combine the terms: term1 - term2
result = term1 - term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))