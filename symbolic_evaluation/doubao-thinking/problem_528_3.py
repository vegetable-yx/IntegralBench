import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e (Euler's number)
e_constant = mp.e

# Calculate e - 1
e_minus_1 = e_constant - 1

# Calculate e^(e - 1)
exp_result = mp.exp(e_minus_1)

# Final result: e^(e - 1) - e
result = exp_result - e_constant

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))