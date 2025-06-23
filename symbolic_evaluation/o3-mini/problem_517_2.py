import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of (pi/2)
sqrt_term = mp.sqrt(mp.pi / 2)

# Calculate the exponential term: e^(1/8)
exp_term = mp.exp(1/8)

# Multiply both terms to get the final result
result = sqrt_term * exp_term

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))