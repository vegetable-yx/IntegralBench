import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# Calculate the square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide the result by 2
term1 = sqrt_pi / 2

# Calculate e^{-1}
exp_term = mp.exp(-1)

# Multiply the two terms together
result = term1 * exp_term

# Print the final result to 10 decimal places
print(mp.nstr(result, n=10))