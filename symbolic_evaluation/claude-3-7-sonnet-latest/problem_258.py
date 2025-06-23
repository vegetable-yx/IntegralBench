import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^{-0.25}
exp_term = mp.exp(-0.25)

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply the components: 2 * e^{-0.25} * sqrt(pi)
result = 2 * exp_term * sqrt_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))