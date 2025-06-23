import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Define the parameter 'a' (example value)
a = mp.mpf(1)

# Calculate individual components of the expression
pi_term = mp.pi
a_squared = a ** 2
exponential_term = mp.exp(-a)
parentheses_term = 1 - exponential_term

# Combine components to compute final result
result = (pi_term / a_squared) * parentheses_term

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))