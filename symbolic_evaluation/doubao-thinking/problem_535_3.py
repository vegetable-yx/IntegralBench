import mpmath as mp

# Set internal decimal precision to 15 for accurate computations
mp.dps = 15

# Calculate the exponential of 3: e^3
exp_val = mp.exp(3)

# Divide the result by 3 to get e^3 / 3
result = exp_val / 3

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))