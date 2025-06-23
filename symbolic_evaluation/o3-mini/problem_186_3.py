import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the parameter b = 1/(5 + sqrt(24))
sqrt24 = mp.sqrt(24)  # Compute square root of 24
denominator = 5 + sqrt24  # Denominator for b
b_val = 1 / denominator  # Parameter b for hypergeometric function

# Set other parameters for the hypergeometric function
a_val = mp.mpf(1)/2  # Parameter a = 1/2
c_val = mp.mpf(3)/2  # Parameter c = 3/2
z_val = -1  # Parameter z = -1

# Compute the hypergeometric function 2F1(a, b; c; z)
hyp_val = mp.hyp2f1(a_val, b_val, c_val, z_val)

# Multiply by pi/8
result = (mp.pi / 8) * hyp_val

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))