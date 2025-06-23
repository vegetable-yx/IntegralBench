import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate e raised to the power of 3
exp_result = mp.exp(3)

# Divide the exponential result by 3
result = exp_result / 3

# Print the final result rounded to 10 decimal places
print(mp.nstr(result, n=10))