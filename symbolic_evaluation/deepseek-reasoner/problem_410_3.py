import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate square root of pi
sqrt_pi = mp.sqrt(mp.pi)

# Divide by 2 to get sqrt(pi)/2 term
sqrt_pi_over_2 = sqrt_pi / 2

# Calculate exponential term e^-1
exp_term = mp.exp(-1)

# Multiply components to get final result
result = sqrt_pi_over_2 * exp_term

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))