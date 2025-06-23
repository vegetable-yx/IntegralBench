import mpmath as mp

# Set precision to 15 decimal places
mp.dps = 15

# Compute natural logarithms
ln2 = mp.log(2)  # ln(2)
ln4 = mp.log(4)  # ln(4)
ln8 = mp.log(8)  # ln(8)

# Calculate cubes of each logarithm
cube_ln2 = ln2 ** 3  # (ln 2)^3
cube_ln4 = ln4 ** 3  # (ln 4)^3
cube_ln8 = ln8 ** 3  # (ln 8)^3

# Multiply the three cubes
product_cubes = cube_ln2 * cube_ln4 * cube_ln8

# Divide by 6 to get final result
result = product_cubes / 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))