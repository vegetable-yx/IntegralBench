import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate e (Euler's number)
e_constant = mp.e

# Compute e - 1
e_minus_1 = e_constant - 1

# Compute e^(e-1) using mp.exp
exp_e_minus_1 = mp.exp(e_minus_1)

# Final calculation: e^(e-1) - e
result = exp_e_minus_1 - e_constant

# Print result with 10 decimal places
print(mp.nstr(result, n=10))