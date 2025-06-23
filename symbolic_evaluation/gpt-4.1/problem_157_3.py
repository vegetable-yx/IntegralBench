import mpmath as mp

# Set the internal decimal places for high precision
mp.dps = 15

# Define the constant factor
factor = 12

# Compute the exponential term: e^{-0.25}
exp_term = mp.exp(-0.25)

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Combine all parts: 12 * e^{-0.25} * sqrt(pi)
result = factor * exp_term * sqrt_pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))