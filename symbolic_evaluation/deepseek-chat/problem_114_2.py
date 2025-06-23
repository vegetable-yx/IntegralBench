import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Get the mathematical constant π (pi)
pi_val = mp.pi

# Calculate the result: -π/4
result = -pi_val / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))