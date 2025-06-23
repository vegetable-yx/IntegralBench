import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Step 1: Compute the mathematical constant e (base of natural logarithm)
e_const = mp.e

# Step 2: Calculate the exponent (e - 1)
exponent = e_const - 1

# Step 3: Compute e raised to the power of (e - 1)
exp_result = mp.exp(exponent)

# Step 4: Subtract e from the result
result = exp_result - e_const

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))