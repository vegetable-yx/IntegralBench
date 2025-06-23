import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e (Euler's number)
euler_e = mp.e

# Compute e - 1
e_minus_1 = euler_e - 1

# Calculate e^(e - 1)
exp_e_minus_1 = mp.exp(e_minus_1)

# Final result: e^(e - 1) - e
result = exp_e_minus_1 - euler_e

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))