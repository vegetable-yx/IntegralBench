import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate Euler's number (e)
euler_e = mp.e

# Compute the exponent (e - 1)
exponent = euler_e - 1

# Calculate e^(e-1) using mpmath's exp function
exp_result = mp.exp(exponent)

# Subtract original e from the result
result = exp_result - euler_e

# Print final value with 10 decimal precision
print(mp.nstr(result, n=10))