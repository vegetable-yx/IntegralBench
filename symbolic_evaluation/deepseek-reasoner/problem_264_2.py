import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate π/4
pi_over_4 = mp.pi / 4

# Compute the hypergeometric function {}_1F_2(1/2; 1, 1; -1)
hyp_term = mp.hyp1f2(0.5, 1, 1, -1)

# Calculate the second term: (π/4) * hypergeometric result
second_term = pi_over_4 * hyp_term

# Compute final result by subtracting terms
result = pi_over_4 - second_term

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))