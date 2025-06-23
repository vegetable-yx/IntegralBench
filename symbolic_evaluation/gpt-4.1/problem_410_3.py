import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate e raised to the power of -1
exp_neg1 = mp.exp(-1)

# Combine the components: (1/2) * sqrt(pi) * e^{-1}
result = 0.5 * sqrt_pi * exp_neg1

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))