import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Compute e^3 using exponential function
exp_val = mp.exp(3)

# Divide the result by 3
result = exp_val / 3

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))