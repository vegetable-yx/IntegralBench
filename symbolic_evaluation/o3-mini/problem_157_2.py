import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the exponential term e^(-1/4)
exp_term = mp.exp(-0.25)

# Multiply the components: 12 * sqrt(pi) * e^(-1/4)
result = 12 * sqrt_pi * exp_term

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))