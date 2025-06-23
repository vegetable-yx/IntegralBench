import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters a and b (example values - can be adjusted)
a_val = 1
b_val = 1

# Compute the argument for the hypergeometric function: (b^2 * a)/16
z_arg = (b_val**2 * a_val) / 16

# Parameters for the hypergeometric function {}_1F_2
a1 = mp.mpf(1)/4  # First parameter: 1/4
b1 = mp.mpf(1)/2  # Second parameter: 1/2
b2 = mp.mpf(3)/4  # Third parameter: 3/4

# Compute the hypergeometric function {}_1F_2(1/4; 1/2, 3/4; z_arg)
hyper_val = mp.hyper([a1], [b1, b2], z_arg)

# Subtract 3/4 from the hypergeometric result
adjusted_hyper = hyper_val - mp.mpf(3)/4

# Multiply by 8 * sqrt(a)
result = 8 * mp.sqrt(a_val) * adjusted_hyper

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))