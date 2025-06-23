import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate e (Euler's number)
e_constant = mp.e

# Compute e - 1
e_minus_1 = e_constant - 1

# Calculate e^(e-1) using mpmath exponential function
exp_result = mp.exp(e_minus_1)

# Final result by subtracting e from the exponential result
result = exp_result - e_constant

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))