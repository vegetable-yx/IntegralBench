import mpmath as mp
mp.dps = 15

# Calculate e (base of natural logarithm)
e_constant = mp.e

# Compute e - 1
e_minus_1 = e_constant - 1

# Calculate e^(e-1) using exp function
exp_result = mp.exp(e_minus_1)

# Final result by subtracting e from the exponential result
result = exp_result - e_constant

print(mp.nstr(result, n=10))