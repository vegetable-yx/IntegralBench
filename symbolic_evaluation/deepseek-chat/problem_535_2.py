import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^3 using exponential function
exp_cubed = mp.exp(3)

# Divide by 3 to get final result
result = exp_cubed / 3

# Output result with exactly 10 decimal places
print(mp.nstr(result, n=10))