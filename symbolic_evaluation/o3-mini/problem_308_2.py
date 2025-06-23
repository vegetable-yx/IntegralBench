import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the first term: π * ln((1 + √2)/2)
# Step 1: Compute √2
sqrt2 = mp.sqrt(2)

# Step 2: Compute the argument (1 + √2)/2
log_arg = (1 + sqrt2) / 2

# Step 3: Compute the natural logarithm of the argument
log_term = mp.log(log_arg)

# Step 4: Multiply by π to get the first term
term1 = mp.pi * log_term

# Calculate the second term: (π/8) * _3F_2(1/2, 1/2, 1/2; 3/2, 3/2; -1)
# Define the parameters for the generalized hypergeometric function
a1 = mp.mpf('0.5')  # 1/2
a2 = mp.mpf('0.5')  # 1/2
a3 = mp.mpf('0.5')  # 1/2
b1 = mp.mpf('1.5')  # 3/2
b2 = mp.mpf('1.5')  # 3/2
z = -1

# Compute the hypergeometric function _3F_2
hyper_val = mp.hyper3f2(a1, a2, a3, b1, b2, z)

# Multiply by π/8 to get the second term
term2 = (mp.pi / 8) * hyper_val

# Sum both terms to get the final result
result = term1 + term2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))