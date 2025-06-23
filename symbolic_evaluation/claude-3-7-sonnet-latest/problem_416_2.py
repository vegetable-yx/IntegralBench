import mpmath as mp

# Set internal precision to 15 decimal places for accurate computation
mp.dps = 15

# Calculate e^(π/4)
exp_term = mp.exp(mp.pi / 4)

# Calculate √2
sqrt_two = mp.sqrt(2)

# Multiply e^(π/4) by √2
numerator = exp_term * sqrt_two - 1

# Divide by 2 to get the final result
result = numerator / 2

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))