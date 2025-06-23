import mpmath as mp
mp.dps = 15

# Calculate cube root of 2 using mpmath power function
cube_root = mp.power(2, mp.mpf(1)/3)

# Divide the cube root by 2 to get final result
result = cube_root / 2

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))