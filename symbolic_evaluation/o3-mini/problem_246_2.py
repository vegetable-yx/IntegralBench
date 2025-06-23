import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator parameters: all are 4
a_params = [4, 4, 4, 4]

# Define denominator parameters: [1/2, 9/2, 8]
b_params = [mp.mpf(1)/2, mp.mpf(9)/2, 8]

# Calculate the generalized hypergeometric function 4F3(1)
hyp_val = mp.hyper(a_params, b_params, 1)

# Compute the constant factor: 9/280
factor = mp.mpf(9)/280

# Multiply to get final result
result = factor * hyp_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))