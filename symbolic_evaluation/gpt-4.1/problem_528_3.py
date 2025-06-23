import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_val = mp.e

# Calculate the exponent: (e - 1)
exponent = e_val - 1

# Compute e raised to the power of (e - 1)
exp_result = mp.exp(exponent)

# Subtract e from the result
result = exp_result - e_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))