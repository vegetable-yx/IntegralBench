import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute e^(π/4)
exp_term = mp.exp(mp.pi/4)

# Compute √2
sqrt2 = mp.sqrt(2)

# Multiply e^(π/4) by √2
numerator = exp_term * sqrt2

# Divide by 2
fraction = numerator / 2

# Subtract 1/2
result = fraction - 0.5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))