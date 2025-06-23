import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Compute e^3 using the exponential function
exp_result = mp.exp(3)

# Divide the result by 3
result = exp_result / 3

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))