import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the difference of digamma functions: ψ(3/4) - ψ(1/4)
digamma_3_4 = mp.digamma(mp.mpf(3)/4)
digamma_1_4 = mp.digamma(mp.mpf(1)/4)
digamma_diff = digamma_3_4 - digamma_1_4

# Compute the logarithmic term: 3 * ln(2)
log_term = 3 * mp.log(2)

# Combine the terms inside the brackets
bracket = digamma_diff + log_term

# Compute the constant factor: (√2 * π) / 8
constant = (mp.sqrt(2) * mp.pi) / 8

# Multiply to get the final result
result = constant * bracket

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))