import mpmath as mp

# Set the internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate e^4
exp_val = mp.exp(4)

# Subtract 1
result = exp_val - 1

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))