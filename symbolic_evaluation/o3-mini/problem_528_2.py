import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant e
e_val = mp.e

# Compute the exponent: e - 1
exponent = e_val - 1

# Compute e^(e-1)
exp_term = mp.exp(exponent)

# Subtract e from the result
result = exp_term - e_val

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))