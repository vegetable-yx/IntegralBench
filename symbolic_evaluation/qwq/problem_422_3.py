import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate the cube root of 16
cube_root_16 = mp.root(16, 3)

# Divide the cube root result by 4
result = cube_root_16 / 4

# Print the final result with 10 decimal places precision
print(mp.nstr(result, n=10))