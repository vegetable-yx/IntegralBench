import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate e-1
e_minus_1 = mp.e - 1

# Compute e raised to the power of (e-1)
exp_term = mp.exp(e_minus_1)

# Subtract e from the exponential term
result = exp_term - mp.e

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))