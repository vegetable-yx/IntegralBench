import mpmath as mp

# Set internal decimal places to 15 for higher precision
mp.dps = 15

# Compute the constant factor: (π * √2) / 2
factor = (mp.pi * mp.sqrt(2)) / 2

# Compute the hypergeometric function: _2F_1(2, 1/4, 3/2, 1/2)
# Parameters: a=2, b=1/4, c=3/2, z=1/2
hyper = mp.hyp2f1(2, mp.mpf(1)/4, mp.mpf(3)/2, mp.mpf(1)/2)

# Multiply the factor and hypergeometric function
result = factor * hyper

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))