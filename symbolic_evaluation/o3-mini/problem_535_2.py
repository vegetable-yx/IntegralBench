import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the exponential of 3: e^3
exp_val = mp.exp(3)

# Divide the result by 3 to get e^3/3
result = exp_val / 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))