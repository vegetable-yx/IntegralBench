import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the argument for the Clausen function: π/3
theta = mp.pi / 3

# Compute the Clausen function of order 3 at θ = π/3
cl3_val = mp.clsin(3, theta)

# Multiply by 4 to get the final result
result = 4 * cl3_val

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))