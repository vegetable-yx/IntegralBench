import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate individual components of the expression
pi_term = mp.pi
sqrt3 = mp.sqrt(3)
linear_term = 6 * sqrt3
constant_term = -12

# Combine terms inside the parentheses
parentheses_sum = pi_term + linear_term + constant_term

# Multiply by pi/3 for final result
result = (mp.pi / 3) * parentheses_sum

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))