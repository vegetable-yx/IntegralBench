import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: sqrt(pi) * Gamma(3/4)
numerator = mp.sqrt(mp.pi) * mp.gamma(3/4)

# Calculate the denominator: 2 * Gamma(5/4)
denominator = 2 * mp.gamma(5/4)

# Compute the constant factor: numerator / denominator
factor = numerator / denominator

# Compute the hypergeometric function: _2F_1(1/4, 1/2; 5/4; 1/2)
hyp_val = mp.hyp2f1(1/4, 1/2, 5/4, 1/2)

# Multiply the factor by the hypergeometric value to get the final result
result = factor * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))