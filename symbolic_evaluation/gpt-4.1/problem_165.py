import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Compute tanh(π) using mpmath's hyperbolic tangent function
tanh_pi = mp.tanh(pi_val)

# Evaluate the expression: (π/2) * tanh(π)
result = (pi_val / 2) * tanh_pi

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))