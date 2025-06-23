import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate cube root of 2
cube_root_2 = mp.root(2, 3)

# Divide the cube root by 2
result = cube_root_2 / 2

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))