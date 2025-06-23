import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Define parameters for the hypergeometric function
a = mp.mpf(1)/4
b = mp.mpf(3)/4
c = mp.mpf(1)
z = mp.mpf(1)

# Compute the hypergeometric function 2F1(1/4, 3/4; 1; 1)
hyp_value = mp.hyp2f1(a, b, c, z)

# Compute the constant factor 2*sqrt(2)
sqrt2 = mp.sqrt(2)
factor = 2 * sqrt2

# Calculate the final result by multiplying components
result = factor * hyp_value

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))