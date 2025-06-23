import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's constant
pi_value = mp.pi

# Calculate (1 - π) component
one_minus_pi = 1 - pi_value

# Multiply components to get final result
result = pi_value * one_minus_pi

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))