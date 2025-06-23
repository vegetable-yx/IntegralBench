import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate mathematical constant e
e_constant = mp.e

# Compute e - 1
e_minus_1 = e_constant - 1

# Calculate e^(e - 1)
exp_e_minus_1 = mp.exp(e_minus_1)

# Final result: e^(e - 1) - e
result = exp_e_minus_1 - e_constant

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))