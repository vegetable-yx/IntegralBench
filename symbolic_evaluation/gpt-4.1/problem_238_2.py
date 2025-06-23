import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Define parameters for the hypergeometric function
a = mp.mpf(5)/mp.mpf(2)   # First parameter: 5/2
b = mp.mpf(1)/mp.mpf(2)   # Second parameter: 1/2
c = mp.mpf(3)/mp.mpf(2)   # Third parameter: 3/2
z = mp.mpf(1)/mp.mpf(4)   # Fourth parameter: 1/4

# Compute the hypergeometric function 2F1(a, b; c; z)
hyper_val = mp.hyp2f1(a, b, c, z)

# Multiply by the coefficient 2
result = 2 * hyper_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))