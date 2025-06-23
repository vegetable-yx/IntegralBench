import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the constant e (base of natural logarithm)
e_const = mp.e

# Calculate the exponent: e - 1
exponent_val = e_const - 1

# Compute exp(e - 1)
exp_result = mp.exp(exponent_val)

# Subtract e from the result
final_result = exp_result - e_const

# Print the final result to 10 decimal places
print(mp.nstr(final_result, n=10))