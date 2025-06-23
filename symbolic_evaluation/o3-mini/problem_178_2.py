import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(2*pi)/32
constant_factor = mp.sqrt(2 * mp.pi) / 32

# Compute the first generalized hypergeometric function: _1F_2(3/2; 3/4, 5/4; -1/4)
hyper1 = mp.hyper([mp.mpf(3)/2], [mp.mpf(3)/4, mp.mpf(5)/4], mp.mpf(-1)/4)

# Compute the second generalized hypergeometric function: _1F_2(3/2; 5/4, 7/4; -1/4)
hyper2 = mp.hyper([mp.mpf(3)/2], [mp.mpf(5)/4, mp.mpf(7)/4], mp.mpf(-1)/4)

# Calculate the difference between the two hypergeometric functions
hyper_diff = hyper1 - hyper2

# Multiply the difference by the constant factor to get the final result
result = constant_factor * hyper_diff

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))