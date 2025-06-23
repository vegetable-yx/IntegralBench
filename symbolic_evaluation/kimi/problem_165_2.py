import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate π/2
pi_over_2 = pi_value / 2

# Calculate e^(-2) using mpmath's exponential function
exp_term = mp.exp(-2)

# Multiply the components to get the final result
result = pi_over_2 * exp_term

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))