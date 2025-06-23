import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the exponential term e^3
exp_term = mp.exp(3)

# Calculate the constant factor 3/2
constant_factor = mp.mpf(3) / 2

# Combine all components: (3/2) * sqrt(pi) * e^3
result = constant_factor * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))