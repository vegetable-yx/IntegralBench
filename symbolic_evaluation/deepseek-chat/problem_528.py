import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_const = mp.e

# Compute the exponent: (e - 1)
exponent = e_const - 1

# Compute e raised to the power (e - 1)
exp_val = mp.exp(exponent)

# Subtract e from the result
result = exp_val - e_const

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))