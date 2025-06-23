import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the numerator: sqrt(pi) * Gamma(3/4)
numerator = mp.sqrt(mp.pi) * mp.gamma(mp.mpf(3)/4)

# Calculate the denominator: 16 * Gamma(11/4)
denominator = 16 * mp.gamma(mp.mpf(11)/4)

# Compute the fraction: numerator / denominator
fraction = numerator / denominator

# Calculate the hypergeometric function: 1F2(1; 7/4, 9/4; -1/4)
hyp = mp.hyper([1], [mp.mpf(7)/4, mp.mpf(9)/4], -mp.mpf(1)/4)

# Multiply the fraction by the hypergeometric function to get the final result
result = fraction * hyp

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))