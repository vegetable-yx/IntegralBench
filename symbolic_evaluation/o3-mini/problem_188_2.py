import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the expression inside the square root: 168
sqrt_168 = mp.sqrt(168)

# Compute the denominator: 13 + sqrt(168)
denom = 13 + sqrt_168

# Calculate the parameter b for the hypergeometric function
b_param = 1 / (2 * denom)

# Compute the hypergeometric function: _2F_1(1, b_param; 1 + b_param; -1)
hyp_val = mp.hyp2f1(1, b_param, 1 + b_param, -1)

# Multiply by pi and divide by 16
result = (mp.pi / 16) * hyp_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))