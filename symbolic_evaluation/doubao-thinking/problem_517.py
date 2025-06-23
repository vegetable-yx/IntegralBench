import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the exponential component e^(1/8)
exponent = mp.mpf(1)/mp.mpf(8)
exp_part = mp.exp(exponent)

# Calculate the square root component sqrt(pi/2)
sqrt_term = mp.sqrt(mp.pi/mp.mpf(2))

# Combine components for final result
result = exp_part * sqrt_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))