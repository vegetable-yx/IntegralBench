import mpmath as mp

# Set the precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the parameters for the hypergeometric function
a = mp.mpf(5)/2  # First parameter
b = mp.mpf(1)/2  # Second parameter
c = mp.mpf(3)/2  # Third parameter
z = mp.mpf(1)/4  # Argument

# Compute the hypergeometric function 2F1(a, b, c, z)
hyper = mp.hyp2f1(a, b, c, z)

# Compute the constant factor: 2 * sqrt(2)
factor = 2 * mp.sqrt(2)

# Multiply to get the final result
result = factor * hyper

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))