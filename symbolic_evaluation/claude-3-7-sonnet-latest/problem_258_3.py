import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the exponential of -0.25
exp_term = mp.exp(-0.25)

# Multiply the components: 256 * sqrt(pi) * e^{-0.25}
result = 256 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))