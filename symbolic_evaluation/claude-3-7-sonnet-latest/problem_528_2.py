import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get the constant e (base of natural logarithm)
base_e = mp.e

# Compute exponent: e - 1
exponent_val = base_e - 1

# Compute e raised to the power of (e - 1)
exp_result = mp.exp(exponent_val)

# Subtract the constant e from the exponential result
final_result = exp_result - base_e

# Print the result with exactly 10 decimal places
print(mp.nstr(final_result, n=10))