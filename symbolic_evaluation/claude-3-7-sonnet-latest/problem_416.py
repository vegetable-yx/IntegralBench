import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate e^(π/4)
exp_term = mp.exp(mp.pi / 4)

# Calculate square root of 2
sqrt_two = mp.sqrt(2)

# Compute the fraction: e^(π/4) / √2
fraction_part = exp_term / sqrt_two

# Subtract 1/2 to get the final result
result = fraction_part - 0.5

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))