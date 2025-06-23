import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define the argument for the hyperbolic cosine function
x = mp.mpf('1.0')

# Compute the hyperbolic cosine of 1.0
result = mp.cosh(x)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))