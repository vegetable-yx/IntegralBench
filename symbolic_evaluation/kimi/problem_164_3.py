import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define the constant coefficient from the analytical expression
constant = mp.mpf('25.5835')

# Calculate π^4 (pi raised to the 4th power)
pi_power4 = mp.pi ** 4

# Compute the final result: constant * π^4
result = constant * pi_power4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))