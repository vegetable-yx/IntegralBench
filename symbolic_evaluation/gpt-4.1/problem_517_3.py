import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# Calculate e raised to the power of 1/8
exp_part = mp.exp(1/8)

# Calculate the square root of (pi divided by 2)
sqrt_part = mp.sqrt(mp.pi / 2)

# Multiply the two parts together
result = exp_part * sqrt_part

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))