import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define the parameters for the hypergeometric function
a1 = mp.mpf(1)/2
a2 = mp.mpf(1)/2
a3 = mp.mpf(1)/2
b1 = mp.mpf(1)
b2 = mp.mpf(3)/2
z = mp.mpf(1)/4

# Compute the generalized hypergeometric function {}_3F_2
hyp_val = mp.hyper3f2(a1, a2, a3, b1, b2, z)

# Multiply by π/4 as per the expression
result = (mp.pi / 4) * hyp_val

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))