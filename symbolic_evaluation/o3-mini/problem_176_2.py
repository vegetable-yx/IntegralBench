import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Define the parameters for the hypergeometric function 3F2
# Numerator parameters: 1/2, 1/2, 1/2
a1 = mp.mpf(1)/2
a2 = mp.mpf(1)/2
a3 = mp.mpf(1)/2
# Denominator parameters: 3/2, 3/2
b1 = mp.mpf(3)/2
b2 = mp.mpf(3)/2
# Argument: 1/4
z_val = mp.mpf(1)/4

# Compute the hypergeometric function 3F2
hyper_term = mp.hyper([a1, a2, a3], [b1, b2], z_val)

# Multiply the result by π/4
result = (mp.pi / 4) * hyper_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))