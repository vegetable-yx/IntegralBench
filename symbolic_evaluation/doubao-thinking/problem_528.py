import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate e (Euler's number)
e_constant = mp.e

# Compute e - 1
e_minus_1 = e_constant - 1

# Calculate e^(e-1)
exp_e_minus_1 = mp.exp(e_minus_1)

# Compute final result: e^(e-1) - e
result = exp_e_minus_1 - e_constant

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))