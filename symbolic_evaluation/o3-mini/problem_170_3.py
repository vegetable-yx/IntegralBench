import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the hypergeometric function value: _2F_1(-1/2, 1/2; 1; 1/2)
hyp_val = mp.hyp2f1(-0.5, 0.5, 1, 0.5)

# Calculate gamma(1/4) squared
gamma_sq = mp.gamma(0.25)**2

# Calculate the logarithm argument: (sqrt(2) + 1) / 2
log_arg = (mp.sqrt(2) + 1) / 2

# Compute the natural logarithm of the argument
log_val = mp.log(log_arg)

# Compute the expression inside the brackets:
# term1 = -pi * (4 * hyp_val + gamma_sq)
term1 = -mp.pi * (4 * hyp_val + gamma_sq)

# term2 = gamma_sq * log_val
term2 = gamma_sq * log_val

# term3 = 8 * hyp_val * log_val
term3 = 8 * hyp_val * log_val

# Sum the terms inside the brackets
bracket_sum = term1 + term2 + term3

# Multiply by sqrt(2)/64 to get the final result
result = (mp.sqrt(2) / 64) * bracket_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))