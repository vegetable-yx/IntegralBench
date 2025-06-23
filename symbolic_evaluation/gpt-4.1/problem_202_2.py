import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is π/2
# Assign π value to a variable
pi_value = mp.pi

# Define the denominator
denominator = 2

# Compute the result: π divided by 2
result = pi_value / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))