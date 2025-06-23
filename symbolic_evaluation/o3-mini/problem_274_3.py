import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign values for a and b (user should modify these as needed)
a = 1.0
b = 1.0

# Compute the argument for the hypergeometric function: (a^2 * b^2)/4
z_arg = (a**2 * b**2) / 4.0

# Calculate the hypergeometric function {}_1F_2((3/2); 2, (5/2); z_arg)
hyp_val = mp.hyper([mp.mpf('3/2')], [2, mp.mpf('5/2')], z_arg)

# Compute the multiplicative factor: a^3 / 3
factor = (a**3) / 3.0

# Calculate the final result
result = factor * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))