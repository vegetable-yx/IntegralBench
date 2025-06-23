import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get the mathematical constant e
e_const = mp.e

# Calculate the exponent: (e - 1)
exponent = e_const - 1

# Compute e raised to the power of (e - 1)
exp_result = mp.exp(exponent)

# Final result: e^(e-1) minus e
result = exp_result - e_const

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))