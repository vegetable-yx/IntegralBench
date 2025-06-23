import mpmath as mp
mp.dps = 15

# Calculate cube root of 2
cube_root_2 = mp.root(2, 3)

# Divide by 2 to get final result
result = cube_root_2 / 2

print(mp.nstr(result, n=10))