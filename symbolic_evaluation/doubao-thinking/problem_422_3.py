import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate cube root of 2
cube_root_2 = mp.root(2, 3)

# Divide the cube root by 2
result = cube_root_2 / 2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))