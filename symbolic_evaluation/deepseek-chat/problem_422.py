import mpmath as mp

# Set internal decimal precision to 15 digits for accurate computations
mp.dps = 15

# Calculate the cube root of 2: 2^(1/3)
cube_root_of_2 = mp.power(2, mp.mpf(1)/3)

# Divide the cube root by 2 to get the final result
result = cube_root_of_2 / 2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))