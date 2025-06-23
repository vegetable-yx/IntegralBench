import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate pi to the fourth power
pi_pow4 = mp.pi ** 4

# Denominator of the expression
denominator = 576

# Compute the final result by dividing pi^4 by 576
result = pi_pow4 / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))