import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute e^4 using mpmath exponential function
exp_value = mp.exp(4)

# Subtract 1 from the exponential result
result = exp_value - 1

# Print the final result with exactly 10 decimal places
print(mp.nstr(result, n=10))