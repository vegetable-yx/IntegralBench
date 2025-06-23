import mpmath as mp
mp.dps = 15  # Set internal precision for calculations

# Calculate cube root of 2 using mpmath's root function
cube_root_2 = mp.root(2, 3)

# Divide the cube root by 2 to get final result
result = cube_root_2 / 2

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))