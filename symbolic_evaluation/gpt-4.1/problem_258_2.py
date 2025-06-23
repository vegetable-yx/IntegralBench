import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step-by-step computation of the analytical expression: 2 * e^{-0.25} * sqrt(pi)

# Compute e^{-0.25} using mp.exp
exp_term = mp.exp(-0.25)

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Multiply the terms: 2 * e^{-0.25} * sqrt(pi)
result = 2 * exp_term * sqrt_pi

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))