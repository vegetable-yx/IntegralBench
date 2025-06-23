import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate π using mpmath's constant
pi = mp.pi

# Calculate e^(-2) using mpmath's exponential function
exp_neg2 = mp.exp(-2)

# Multiply π/2 by e^(-2)
result = (pi / 2) * exp_neg2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))