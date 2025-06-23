import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the numerator: sqrt(pi) * Gamma(3/4)
numerator = mp.sqrt(mp.pi) * mp.gamma(3/4)

# Compute the denominator: 2 * Gamma(5/4)
denominator = 2 * mp.gamma(5/4)

# Compute the fraction: numerator / denominator
fraction = numerator / denominator

# Compute the hypergeometric function: 2F1(1/2, 3/4; 5/4; 1/2)
hyp = mp.hyp2f1(1/2, 3/4, 5/4, 1/2)

# Multiply the fraction by the hypergeometric function
result = fraction * hyp

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))