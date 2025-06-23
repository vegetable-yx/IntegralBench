import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Assign the constant 3
constant_factor = 3

# Get the value of π
pi_value = mp.pi

# Compute 3π
result = constant_factor * pi_value

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))