import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Compute the exponential of -1 (which is e^{-1})
exp_minus_one = mp.exp(-1)

# Combine the components: (sqrt(pi) / 2) * e^{-1}
result = (sqrt_pi / 2) * exp_minus_one

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))