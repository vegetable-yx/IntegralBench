import mpmath as mp

# Set internal precision to 15 decimal places for calculations
mp.dps = 15

# Define the constant factor
factor = 3

# Access the mathematical constant π
pi_val = mp.pi

# Multiply the factor by π to get the result
result = factor * pi_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))