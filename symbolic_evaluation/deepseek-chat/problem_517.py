import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the constant factor: sqrt(pi/2)
sqrt_arg = mp.pi / 2  # Compute pi divided by 2
sqrt_term = mp.sqrt(sqrt_arg)  # Take square root of pi/2

# Calculate the exponential term: e^(1/8)
exp_arg = mp.mpf(1)/8  # Compute exponent 1/8 using mpmath float
exp_term = mp.exp(exp_arg)  # Raise e to the power of 1/8

# Multiply both terms to get final result
result = sqrt_term * exp_term

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))