import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Define parameters for the hypergeometric function
a = mp.mpf(5)/2  # First parameter
b = mp.mpf(1)/2  # Second parameter
c = mp.mpf(3)/2  # Third parameter
z = mp.mpf(1)/4  # Argument

# Compute the hypergeometric function value
hyp_val = mp.hyp2f1(a, b, c, z)

# Multiply by 2 as per the expression
result = 2 * hyp_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))