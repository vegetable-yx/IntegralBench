import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Calculate exponential term e^(-1/4)
exp_term = mp.exp(mp.mpf('-0.25'))

# Multiply components together with coefficient 12
result = 12 * sqrt_pi * exp_term

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))