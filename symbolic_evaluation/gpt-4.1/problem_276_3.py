import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the hypergeometric function 0F1(;3/2;9)
hypergeometric_term = mp.hyp0f1(mp.mpf(3)/2, 9)

# Calculate the square root of 3
sqrt_3 = mp.sqrt(3)

# Combine components for final result
result = 2 * sqrt_3 * hypergeometric_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))