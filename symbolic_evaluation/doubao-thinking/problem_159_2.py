import mpmath as mp

# Set internal decimal places to 15 for high precision
mp.dps = 15

# Calculate e^2
exp_pos = mp.exp(2)

# Calculate e^{-2}
exp_neg = mp.exp(-2)

# Sum the exponential terms
exp_sum = exp_pos + exp_neg

# Multiply by 4
result = 4 * exp_sum

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))