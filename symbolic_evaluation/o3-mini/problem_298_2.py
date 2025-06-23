import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define parameters for the generalized hypergeometric function
# Numerator parameters: [1/2, 1/2, 1/2]
a1 = mp.mpf(1)/2
a2 = mp.mpf(1)/2
a3 = mp.mpf(1)/2
# Denominator parameters: [1, 3/2]
b1 = 1
b2 = mp.mpf(3)/2
# Argument
z = mp.mpf(1)/4

# Compute the hypergeometric function {}_3F_2
hyper_val = mp.hyper([a1, a2, a3], [b1, b2], z)

# Compute π^2
pi_squared = mp.pi**2

# Combine terms: (π^2 / 4) * hypergeometric result
result = (pi_squared / 4) * hyper_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))