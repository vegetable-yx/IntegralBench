import mpmath as mp

# Set internal decimal precision to 15 for accurate computation to 10 decimal places
mp.dps = 15

# Calculate the components of the expression
# π (pi) constant
pi_val = mp.pi

# √2 (square root of 2)
sqrt2_val = mp.sqrt(2)

# Hypergeometric function {}_2F_1(2, 1/4; 1; 1/4)
hyp_val = mp.hyp2f1(2, 0.25, 1, 0.25)

# Compute the final result: π * √2 * {}_2F_1(...)
result = pi_val * sqrt2_val * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))