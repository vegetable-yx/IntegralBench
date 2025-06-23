import mpmath as mp

# Set internal decimal places for high precision
mp.dps = 15

# Calculate the cube root of 2
cube_root_2 = mp.root(2, 3)

# Divide the cube root by 2 to get the result
result = cube_root_2 / 2

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))