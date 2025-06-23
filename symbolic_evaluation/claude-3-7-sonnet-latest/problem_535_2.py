import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Calculate e raised to the power of 3
exp_val = mp.exp(3)

# Divide the result by 3
result = exp_val / 3

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))