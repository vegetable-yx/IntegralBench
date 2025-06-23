import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_constant = mp.e

# Calculate the exponent: e - 1
exponent = e_constant - 1

# Compute e raised to the power of (e - 1)
exp_term = mp.exp(exponent)

# Subtract e from the result
result = exp_term - e_constant

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))