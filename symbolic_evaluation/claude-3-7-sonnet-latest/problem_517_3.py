import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate e^(1/8)
exp_part = mp.exp(1/8)

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate the numerator: e^(1/8) * sqrt(pi)
numerator = exp_part * sqrt_pi

# Calculate the denominator: sqrt(2)
denominator = mp.sqrt(2)

# Compute the final result: numerator / denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))